import serial
import time
# from pynput.keyboard import Key, Listener

class SerialPort:

    def __init__(self, port: str = '/dev/tty.HC-05-DevB'):
        self.port = port
        self.ser = serial.Serial(self.port)

        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.ser.parity = serial.PARITY_NONE #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits
        #ser.timeout = None          #block read
        self.ser.timeout = 1            #non-block read
        #ser.timeout = 2              #timeout block read
        self.ser.xonxoff = False     #disable software flow control
        self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

        self.ser.flushInput()
        self.ser.flushOutput()

        print('connected')

        self.run = True

        def mainloop(self):
            while True:
                print(i)
                bytesToRead = ser.inWaiting()
                data_bytes = ser.read(bytesToRead)
                print(data_bytes)

                data = str(data_bytes).split('\r\n')

                data_floats = [[float(z) for z in (try_convert(j) for j in i) if z] for i in data]

                if not self.run:
                    self.ser.close()
                    break

                # data_raw = ser.readline()
                #
                # if len(data_raw):
                #     print(data_raw)
                time.sleep(0.5)

        @staticmethod
        def try_convert(val):
            try:
                return float(val)
            except (ValueError, TypeError):
                pass

# def on_press(key):
#     global ser
#     ser.close()
#     sys.exit()
#
# with Listener(
#         on_press=on_press) as listener:
#     listener.join()

# for i in range(20):
#     print(i)
#     bytesToRead = ser.inWaiting()
#     data_bytes = ser.read(bytesToRead)
#     print(data_bytes)
#
#     data = str(data_bytes).split('\r\n')
#
#     data_floats = [[float(z) for z in (try_convert(j) for j in i) if z] for i in data]
#
#     # data_raw = ser.readline()
#     #
#     # if len(data_raw):
#     #     print(data_raw)
#     time.sleep(0.5)
#
# ser.close()

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
