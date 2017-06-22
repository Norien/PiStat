# PiStat by [@Norien](https://gitter.im/norien)

Using Python run shell commands and output results into ```stats.json``` for use in HTML or Home Assistant


 - Usage ```Python /path/to/stats.py > stats.json```

 
SAMPLE OUTPUTS
* JSON
``` 
{"load_average": {"fifteen_minutes": 16.0, "one_minute": 0.0, "five_minutes": 11.0}, "processes": {"process_running": "0", "smbd": "online", "bluetooth": "online", "process_total": "99", "ssh": "online"}, "network": {"lan_ip": "192.168.1.70", "lan_mac": "b2:48:pu:1c:84:0d", "hostname": "raspberrypizero"}, "system": {"kernel": "4.9.24+", "uptime": "1 day, 22:36:32.370000", "server_time": "2017-06-22 10:06:02", "users": "0", "last_boot_day": "2017-06-20", "release": "Raspbian GNU/Linux 8.0 (jessie)", "last_boot_time": "11:29:30"}, "memory": {"total": 434, "used": 397}, "disk_space": {"disk_space_use": "16", "disk_space_size": "7.2", "disk_space_available": "5.8", "disk_space_used": "1.1"}, "cpu": {"cpu_frequency": 1000, "cpu_model": "ARMv6-compatible processor rev 7 (v6l)"}, "temperature": {"system_temp": 35}}
```

* HTML
```
System	
OS	Raspbian GNU/Linux 8.0 (jessie)
Kernel	4.9.24+
Uptime	1 day, 22:51:32.150000
Last Boot	2017-06-20 11:29:30
Server Time	2017-06-22 10:21:02
Current User(s)	0 Connected

Load Average	
Since 1 minute	0 %
Since 5 minutes	7 %
Since 15 minutes	13 %

CPU	
Model	ARMv6-compatible processor rev 7 (v6l)
Frequency	1000 MHz

Memory	
RAM	397 Mb free of 434 Mb

Network	
Hostname	raspberrypizero
IP LAN	192.168.1.70
Mac Address	b2:48:pu:1c:84:0d

Disk Space	
Use	16 %
Total Size	7.2 GB
Available Space	5.8 GB
Used	1.1 GB

Processes	
Total Processes	100
SMB	online
Bluetooth	online
SSH	online

Temperature	
System Temp	35C
```