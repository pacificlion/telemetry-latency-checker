import serial
import time
import json
from datetime import datetime
import random
import string

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

date_format_str = '%d/%m/%Y %H:%M:%S.ffffff%f'
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=57600)
ser.reset_input_buffer()
timestamp = 0
while True:
    
    time.sleep(0.02)
    data ={}
    

    data["ts"] = timestamp
    data["payload"] = randStr(chars=string.ascii_lowercase, N=1000)
    now = datetime.now()
    current_time = now.strftime(date_format_str)
    data["time"] = current_time
    
    timestamp +=1
    
    data=json.dumps(data)
    data = data+"\n"
    
    ser.write(data.encode('ascii'))
    ser.flush() 
    
    print("sending data",timestamp,", of bytes:",data.__sizeof__())