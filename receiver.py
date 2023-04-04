# Receiver
import serial
import json
import sys
from datetime import datetime
import pandas as pd

date_format_str = '%d/%m/%Y %H:%M:%S.ffffff%f'
ser = serial.Serial(port='/dev/ttyUSB1',baudrate=57600)
ser.reset_input_buffer()
first_ts = -1
last_ts = -1
lost_packets = 0
packets_received=0
latency = 0


def signal_handler():
    print('You pressed Ctrl+C!')
    print("============================")
    print("first time stamp",first_ts)
    print("last time stamp",last_ts)
    print("packets lost or out of order",lost_packets)
    print("# of packets processed",packets_received)
    if packets_received>0:
        print("average latency#",latency/packets_received,"ms")
    sys.exit(0)
    
    
while True:
    try:
        data = ser.readline().decode("utf-8")
        if data=="":
            continue
        try:
            now = datetime.now()
            dict_json = json.loads(data)
            curr_ts = dict_json['ts']
            start_time = dict_json['time']
            if first_ts == -1:
                first_ts = curr_ts
                last_ts = curr_ts
                
            if last_ts >= curr_ts:
                print("packet out of order, expected  :", (last_ts+1),"received this instead:",curr_ts)
                lost_packets+=1
                continue
            start = pd.to_datetime(start_time, format=date_format_str)
            
            
            # current_time = now.strftime(date_format_str)
            # print("voila diff",(now-start).microseconds)
            latency+=((now-start).microseconds/1000)
            last_ts = curr_ts
            packets_received+=1
        except json.JSONDecodeError as e:
            print("JSON error:",e)
    except KeyboardInterrupt:
        signal_handler()