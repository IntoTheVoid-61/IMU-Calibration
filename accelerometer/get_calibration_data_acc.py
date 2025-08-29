import serial
import time
import numpy as np
import re



#-------------------GENERAL_PARAMETERS----------------------------------#
SERIAL_PORT = "COM4"
BAUD_RATE = 115200 # Make sure it is equal to the Baud rate in Arduino IDE
OUTPUT_FILE = "data_text_files/acc_data_for_magneto.txt" # Change this to your specific file
NUM_OF_SAMPLES_PER_ORIENTATION = 500
NUM_OF_TOTAL_SAMPLES = 100 # This controls in how many orientations you want to gather data

#-------------------END_OF_GENERAL_PARAMETERS----------------------------------#


#-------------------CONNECTION_TO_SENSORS--------------------------------------#
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE,timeout=1)
    print(f"Connected to {SERIAL_PORT} at baud rate {BAUD_RATE}")
except serial.SerialException as e:
    print(f"Failure to connect: {e}")
    exit(0)

time.sleep(2) # Da se stabilizira

#-------------------END_CONNECTION_TO_SENSORS--------------------------------------#

#--------------------------COLLECTION_LOOP------------------------------------------#
print(f"Starting data collection")

for i in range(NUM_OF_TOTAL_SAMPLES):
    print(f"\nPlace IMU in position {i} and keep it stationary!")
    input("Press Enter when ready...")
    raw_data = []
    attempts = 0
    while len(raw_data) < NUM_OF_SAMPLES_PER_ORIENTATION and attempts < NUM_OF_SAMPLES_PER_ORIENTATION * 2:
        try:    # Catcha ce ni pricakovan starting byte
            line = ser.readline().decode("utf-8").strip()
            if line:
                if "Scaled. Acc" in line:
                    numbers = re.findall(r'[-+]?[0-9]+\.[0-9]+', line)
                    if len(numbers) >= 10:
                        ax,ay,az = map(lambda x: float(x) / 1000, numbers[0:3]) # This is necessary since the data is in units of mgs
                        raw_data.append([ax, ay, az])
                    else:
                        print(f"Missing data, malformed error!   Error counter: {attempts}")
                        attempts += 1
                else:
                    print(f"Missing data, could not find beggining of package!   Error counter: {attempts}")
                    attempts += 1
            else:
                print(f"Empty line! error : {attempts}")
                attempts += 1
        except Exception as e:
            print(f"Invalid data!.... retrying")
            attempts += 1

    print(f"Saving data to {OUTPUT_FILE}, for orientation {i}")
    raw_data = np.array(raw_data)
    avg = np.mean(raw_data, axis=0)
    print(f"x_avg = {avg[0]:.4f}    II  y_avg = {avg[1]:.4f}    II  z_avg = {avg[2]:.4f}")

    try:
        with open(OUTPUT_FILE, "a") as f: # append mode => meaning it adds data not overwrites
            f.write(f"{avg[0]:.4f}\t{avg[1]:.4f}\t{avg[2]:.4f}\n")
            print(f"Data sucesfully saved to output file: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Failed to save data to output file: {OUTPUT_FILE}")