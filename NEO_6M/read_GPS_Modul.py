import io
import serial
import sys
import logging


logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

ser = serial.Serial(
        port = '/dev/ttyAMA0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while True:
        try:
                line = sio.readline()
                
                new_line = line.split(sep =",")
                
                logger.debug (new_line)
                
                speed_knots = 'not available'
                speed_km_h = 'not available'
                
                if new_line[0] == '$GPRMC':
                    if new_line[2] == 'A':
                        speed_knots = float(new_line[7])
                        speed_km_h = 1.852 * speed_knots
                        
                    print("Speed in knots: ", speed_knots)
                    print("Speed in km/h: ", speed_km_h)
        except KeyboardInterrupt:
                print("\nProgram terminated by user.")
                break
        except serial.SerialException as e:
                logger.error('SerialException: {}'.format(e))
                break
        except UnicodeDecodeError as e:
                logger.error('UnicodeDecodeError: {}'.format(e))
                continue
