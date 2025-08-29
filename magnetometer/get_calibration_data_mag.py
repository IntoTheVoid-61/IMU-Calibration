import serial
import time
import numpy as np
import re

#--------------------------PARAMETERS------------------------------#

SERIAL_PORT = "COM4"
BAUD_RATE = 115200
OUTPUT_FILE = "data_text_files/mag_data_for_magneto.txt" # relative path to the file where the raw accelerometer data will be stored, change as you wish
DURATION = 60 # Number of seconds for which you will collect data

#--------------------------END_OF_PARAMETERS------------------------------#



#--------------------------CONNECTION-------------------------------------#
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at baud rate {BAUD_RATE}")
except serial.serialutil.SerialException as e:
    print(f"Failed to connect to {SERIAL_PORT}. {e}")
    exit(0)

time.sleep(5)   # To stabilize the signal

#--------------------------END_OF_CONNECTION------------------------------#

def collect_magnetometer_data(duration = DURATION):
    error_counter = 0
    print(f"collecting data for {duration} seconds, rotate sensor in 8 shape")
    start_time = time.time()
    mag_data = []

    while time.time() - start_time < duration:
        try:
            line = ser.readline().decode("utf-8").strip()
            if line:
                if "Scaled. Acc" in line:
                    numbers = re.findall(r'[-+]?[0-9]+\.[0-9]+', line)
                    if len(numbers) >= 10:
                        mx, my, mz = map(float, numbers[6:9])
                        mag_data.append([mx, my, mz])
                    else:
                        print(f"Missing data!   Error counter: {error_counter}")
                        error_counter += 1
                else:
                    print(f"Malformed data!  Error counter: {error_counter}")
                    error_counter += 1
            else:
                print(f"Empty data line: {line}     Error counter: {error_counter}")
                error_counter += 1
        except Exception as e:
            print(f"error: {e}      Error counter: {error_counter}")
            error_counter += 1
            continue
        time.sleep(0.05) # 1/0.05 = 20Hz sampling rate

    with open(OUTPUT_FILE, "w") as f:
        for mag in mag_data:
            f.write(f"{mag[0]}\t{mag[1]}\t{mag[2]}\n")
    print(f"Collected {len(mag_data)} samples. Data saved to {OUTPUT_FILE}")

    return None

collect_magnetometer_data()
