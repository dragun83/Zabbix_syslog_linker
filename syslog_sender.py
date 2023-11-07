#!/bin/python3

from pyzabbix import ZabbixSender, ZabbixMetric, ZabbixAPI
import socket

zbx_srv = '127.0.0.1'                                 # Адрес сервера Zabbix
syslog_key = 'zabbix_syslog'                          # Ключ данных
zbx_url = 'http://127.0.0.1/zabbix/'
zbx_user = 'Admin'
zbx_pass = 'zabbix'
syslog_port = 514
syslog_interface = "172.22.101.103"
syslog_buffer = 1024


def get_zbx_hostname(ip_addr):
    api = ZabbixAPI(url = zbx_url, user = zbx_user, password = zbx_pass)
    ret = api.host.get(output = ['host'], filter = {'ip': ip_addr})
    return ret[0]['host']

def send_msg_to_zbx(ip_addr, text):
    messages = []
    m = ZabbixMetric(get_zbx_hostname(ip_addr), syslog_key, text)
    messages.append(m)
    snd = ZabbixSender( zbx_srv)
    snd.send(messages)
    
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)    
s.bind((syslog_interface, syslog_port))

while(True):
    dat = s.recvfrom(syslog_buffer)
    if(dat): 
      send_msg_to_zbx(dat[1],dat[0].decode('utf-8'))
      print("We got message and send it to Zabbix!")
