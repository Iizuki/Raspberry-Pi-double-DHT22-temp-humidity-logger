import Adafruit_DHT

#Script for testing two DHT22 sensors
DHT_SENSOR_TYPE = Adafruit_DHT.DHT22

#Pins where the sensors are connected
DHT1_PIN = 4
DHT2_PIN = 18
PINLIST = [DHT1_PIN, DHT2_PIN]
while True:
    for DHT_PIN in PINLIST:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, DHT_PIN)
        print("Sensor", PINLIST.index(DHT_PIN), ": ", sep='', end='')
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
