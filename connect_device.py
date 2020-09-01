import serial

ser = serial.Serial('/dev/tty.HC-05-DevB', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

while True:
    bytesToRead = ser.inWaiting()
    data_raw = ser.read(bytesToRead)

    # data_raw = ser.readline()

    print(data_raw)

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
