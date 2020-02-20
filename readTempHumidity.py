import Adafruit_DHT

#Function to read data from DHT22 sensor
def readTempHumidity(pin, result, index):
    DHT_SENSOR_TYPE = Adafruit_DHT.DHT22
    
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, pin)

    #Save values
    result[index] = humidity
    result[index+1] = temperature
    return True
