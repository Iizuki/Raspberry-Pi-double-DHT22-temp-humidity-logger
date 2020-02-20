import os
import time
import readTempHumidity as read
from threading import Thread

#Pins where the DHT22 sensors are connected.
DHT1_PIN = 4
DHT2_PIN = 18
PINLIST = [DHT1_PIN, DHT2_PIN]

#Threads will save their results here
result = [None] * 4

#Start threads to read sensors
threads = []
index = 0
for pin in PINLIST:
    thread = Thread(target=read.readTempHumidity, args=[pin, result, index])
    thread.start()
    threads.append(thread)
    index += 2
    
#Chech if this is the first write to the log file
try:
    f = open('/home/pi/puer-project/humidityTempLog.csv', 'a+')
    if os.stat('/home/pi/puer-project/humidityTempLog.csv').st_size == 0:
            f.write('Date,Time,Temperature1,Temperature2,Humidity1,Humidity2\r\n')
except:
    pass

#Wait for the threads to finish
for thread in threads:
    thread.join()

#Write measured values to logfile
hum1 = result[0]
temp1 = result[1]
hum2 = result[2]
temp2 = result[3]
f.write('{0},{1},{2:0.1f}*C,{3:0.1f}*C,{4:0.1f}%,{5:0.1f}%\r\n'.format(time.strftime('%d/%m/%y'), time.strftime('%H:%M'), temp1, temp2, hum1, hum2))
