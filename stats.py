import json
import subprocess
from datetime import timedelta

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds = uptime_seconds))

release = subprocess.check_output('/usr/bin/lsb_release -ds', shell=True)
kernel = subprocess.check_output('/bin/uname -r', shell=True)
last_boot_day = subprocess.check_output("uptime -s | awk '{print $1}'", shell=True)
last_boot_time = subprocess.check_output("uptime -s | awk '{print $2}'", shell=True)
users = subprocess.check_output('who | wc -l', shell=True)
server_time = subprocess.check_output("/bin/date '+%F %T'", shell=True)

one_minute = subprocess.check_output("cat /proc/loadavg | awk '{print $1}'", shell=True)
five_minutes = subprocess.check_output("cat /proc/loadavg | awk '{print $2}'", shell=True)
fifteen_minutes = subprocess.check_output("cat /proc/loadavg | awk '{print $3}'", shell=True)

cpu_model = subprocess.check_output("cat /proc/cpuinfo | grep -i '^model name' | awk -F': ' '{print $2}' | head -1 | sed 's/ \+/ /g'", shell=True)
cpu_frequency = subprocess.check_output("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq", shell=True)

memory_total = subprocess.check_output("/usr/bin/free -tm | grep -i Mem: | awk '{print $2}'", shell=True)
memory_used = subprocess.check_output("/usr/bin/free -tm | grep -i Mem: | awk '{print $4}'", shell=True)
memory_gpu = subprocess.check_output("vcgencmd get_mem gpu", shell=True)

hostname = subprocess.check_output('hostname', shell=True)
lan_ip = subprocess.check_output("ip route get 8.8.8.8 | awk '{print $NF; exit}'", shell=True)
lan_mac = subprocess.check_output("cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address", shell=True)

disk_space_size = subprocess.check_output("df -hl / | sed '1 d' | grep -iv '^Filesystem|Sys.' | grep -vE '^tmpfs|udev' | sort | head -5 | sed s/^/'  '/ | awk '{print $2}'", shell=True)
disk_space_used = subprocess.check_output("df -hl / | sed '1 d' | grep -iv '^Filesystem|Sys.' | grep -vE '^tmpfs|udev' | sort | head -5 | sed s/^/'  '/ | awk '{print $3}'", shell=True)
disk_space_available = subprocess.check_output("df -hl / | sed '1 d' | grep -iv '^Filesystem|Sys.' | grep -vE '^tmpfs|udev' | sort | head -5 | sed s/^/'  '/ | awk '{print $4}'", shell=True)
disk_space_use = subprocess.check_output("df -hl / | sed '1 d' | grep -iv '^Filesystem|Sys.' | grep -vE '^tmpfs|udev' | sort | head -5 | sed s/^/'  '/ | awk '{print $5}'", shell=True)

system_temp = subprocess.check_output('cat /sys/class/thermal/thermal_zone0/temp | cut -c1-2', shell=True)

process_total = subprocess.check_output('ps -e h | wc -l', shell=True)
process_running = subprocess.check_output('ps r h | wc -l', shell=True)
ssh = subprocess.check_output("ps -ef | grep ssh | grep -v grep | awk  '{print $3}' | head -1", shell=True)
ssh_status = 'online' if ssh.strip() == '1' else 'offline'
smbd = subprocess.check_output("ps -ef | grep smbd | grep -v grep | awk  '{print $3}' | head -1", shell=True)
smbd_status = 'online' if smbd.strip() == '1' else 'offline'
bluetooth = subprocess.check_output("ps -ef | grep bluetooth | grep -v grep | awk  '{print $3}' | head -1", shell=True)
bluetooth_status = 'online' if bluetooth.strip() == '1' else 'offline'
flic = subprocess.check_output("ps -ef | grep flicd | grep -v grep | awk  '{print $3}' | head -1", shell=True)
flic_status = 'online' if flic.strip() == '1' else 'offline'
kodi = subprocess.check_output("ps -ef | grep kodi | grep -v grep | awk  '{print $3}' | head -1", shell=True)
kodi_status = 'online' if kodi.strip() == '1' else 'offline'
vnc = subprocess.check_output("ps -ef | grep vnc | grep -v grep | awk  '{print $3}' | head -1", shell=True)
vnc_status = 'online' if vnc.strip() == '1' else 'offline'

out = {}

out["system"] = {}
out["system"]["release"] = release.strip()
out["system"]["kernel"] = kernel.strip()
out["system"]["uptime"] = str(uptime.strip())
out["system"]["last_boot_day"] = last_boot_day.strip()
out["system"]["last_boot_time"] = last_boot_time.strip()
out["system"]["users"] = users.strip()
out["system"]["server_time"] = server_time.strip()

out["load_average"] = {}
out["load_average"]["one_minute"] = round(100 * float(one_minute.strip()))
out["load_average"]["five_minutes"] = round(100 * float(five_minutes.strip()))
out["load_average"]["fifteen_minutes"] = round(100 * float(fifteen_minutes.strip()))

out["cpu"] = {}
out["cpu"]["cpu_model"] = cpu_model.strip()
out["cpu"]["cpu_frequency"] = int(cpu_frequency.strip()) / 1000

out["memory"] = {}
out["memory"]["total"] = int(memory_total)
out["memory"]["used"] = int(memory_used)
out["memory"]["gpu"] = memory_gpu.strip()[4:-1]

out["network"] = {}
out["network"]["hostname"] = hostname.strip()
out["network"]["lan_ip"] = lan_ip.strip()
out["network"]["lan_mac"] = lan_mac.strip()

out["disk_space"] = {}
out["disk_space"]["disk_space_size"] = disk_space_size.strip()[:-1]
out["disk_space"]["disk_space_used"] = disk_space_used.strip()[:-1]
out["disk_space"]["disk_space_available"] = disk_space_available.strip()[:-1]
out["disk_space"]["disk_space_use"] = disk_space_use.strip()[:-1]

out["temperature"] = {}
out["temperature"]["system_temp"] = int(system_temp)

out["processes"] = {}
out["processes"]["process_total"] = process_total.strip()
out["processes"]["process_running"] = process_running.strip()
out["processes"]["ssh"] = ssh_status.strip()
out["processes"]["smbd"] = smbd_status.strip()
out["processes"]["bluetooth"] = bluetooth_status.strip()
out["processes"]["flic"] = flic_status.strip()
out["processes"]["kodi"] = kodi_status.strip()
out["processes"]["vnc"] = vnc_status.strip()

print json.dumps(out)