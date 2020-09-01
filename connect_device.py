import serial
import time
from pynput.keyboard import Key, Listener
import sys

ser = serial.Serial('/dev/tty.HC-05-DevB', 9600, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
# ser.flushInput()
# ser.flushOutput()

print('connected')

def on_press(key):
    global ser
    ser.close()
    sys.exit()

with Listener(
        on_press=on_press) as listener:
    listener.join()

while True:
    # bytesToRead = ser.inWaiting()
    # data_raw = ser.read(bytesToRead)
    data_raw = ser.read(100)
    # data_raw = ser.readline()

    # print(len(data_raw))
    if len(data_raw):
        print(data_raw)

    time.sleep(0.1)

# import time
# import bluetooth
#
# while True:
#
#     results = bluetooth.discover_devices(duration=4, lookup_names = True)
#     print(results)
#     if (results!=None):
#         for addr, name in results:
#             print("{0} - {1}".format(addr, name))
#
#     time.sleep(60)
