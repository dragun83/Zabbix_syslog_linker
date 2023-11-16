# SYSLOG COLLECTOR FOR ZABBIX

Autor Aleksey Dargunov (dragun83@gamil.com)

## Reqirenments

1. Python3.x
2. PyZabbix library


## Installation

1. Check your Python instllation path and correct *syslog_sender.py*  string  *#!/bin/python3* string if need.

2. Put *syslog_sender* to */usr/local/bin*

3. Create systemctl service *sudo systemctl edit --full syslog_sender.service*

4. Put the code below in it.
```
[Unit]
Description=Small syslog to Zabbix connector
After=multi-user.target

[Service]
ExecStart=/usr/local/bin/syslog_sender.py
Type=simple

[Install]
WantedBy=multi-user.target
```

5. Enable and run service.
```
#> systemctl enable syslog_sender.service
#> systemctl start syslog_sender.sevice
```
6. Create template in Zabbix with name **Syslog**
7. Create **trapper item** [manual](https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/trapper)

8. Create **host** and attache **Syslog** template to it. IP address is the key to identificate syslog source. [manual](https://www.zabbix.com/documentation/current/en/manual/config/hosts/host)

Now in "Last data" you can see syslog messages.
