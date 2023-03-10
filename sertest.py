import serial
import io
ser = serial.Serial('/dev/ttyUSB0', 38400)
print(ser.name)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

sio.write(unicode("hello\n"))
sio.flush() # it is buffering. required to get the data out *now*
hello = sio.readline()
print(hello == unicode("hello\n"))
