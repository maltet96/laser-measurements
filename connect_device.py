import serial
import time
from pynput.keyboard import Key, Listener
import sys

ser = serial.Serial('/dev/tty.HC-05-DevB', 9600, timeout=1)#, xonxoff=False, rtscts=False, dsrdtr=False)
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

ser.flushInput()
ser.flushOutput()

print('connected')

# def on_press(key):
#     global ser
#     ser.close()
#     sys.exit()
#
# with Listener(
#         on_press=on_press) as listener:
#     listener.join()

for i in range(10000000):
    # bytesToRead = ser.inWaiting()
    # data_raw = ser.read(bytesToRead)
    # data_raw = ser.read(100)
    data_raw = ser.readline()
    print(i)
    # if len(data_raw):
    print(data_raw)
    if len(data_raw):
        import pdb;pdb.set_trace()
ser.close()

    # time.sleep(0.1)

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
