#!/usr/bin/python3

from datetime import datetime
import json, subprocess

now = datetime.now()

blocks = subprocess.check_output("tail -1 /var/lib/docker/volumes/generated_bitcoin_datadir/_data/debug.log | awk '{printf $5}'",shell=True).decode('utf-8')
percent = subprocess.check_output("tail -1 /var/lib/docker/volumes/generated_bitcoin_datadir/_data/debug.log | awk '{printf $10}'",shell=True).decode('utf-8')

temp = int(subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp",shell=True))
cpuload = subprocess.check_output("cat /proc/loadavg",shell=True).decode('utf-8')
memused = subprocess.check_output("vmstat -s | grep 'used memory' | awk '{printf $1}'",shell=True).decode('utf-8')
dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

blocks = blocks[7:]
percent = float(percent[9:])

percent = "{:.1%}".format(percent)

temp = round(temp / 1000, 1)
memused = round(int(memused) / 1000000,2)
cpu15min = cpuload[10:14]

with open('/root/log.csv','a+') as f:
    f.write(str(blocks) + ';' + str(percent) + ';' + str(temp) + ';' + cpu15min + ';' + cpu15min + 'G;' + dt_string + '\n')