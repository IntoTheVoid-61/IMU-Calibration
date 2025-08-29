import serial
import time
import numpy as np

SERIAL_PORT = "COM3"
BAUD_RATE = 9600
NUMBER_OF_SAMPLES = 1000




# Connect to serial port
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at baud rate {BAUD_RATE}")
except serial.SerialException as e:
    print(f"Failed to connect to {e}")
    exit(0)

time.sleep(2)  # Stabilize connection


# Collect data
def estimate_gyro_bias(samples=NUMBER_OF_SAMPLES):
    print("Estimating gyro bias, keep IMU stationary...")
    gyro_data = []
    for _ in range(samples):
        line = ser.readline().decode("utf-8").strip()
        if line:
            data = line.split("\t")
            if len(data) == 8:
                gx, gy, gz = map(lambda x: float(x) * (np.pi / 180), numbers[3:6]) # This is necesarry since we get data in units DPS
                gyro_data.append([gx, gy, gz])
        time.sleep(0.01)

    if gyro_data:
        bias = np.mean(gyro_data, axis=0)  # Average over samples
        print(f"Gyro biases (rad/s): x={bias[0]:.4f}, y={bias[1]:.4f}, z={bias[2]:.4f}")
        return bias
    else:
        print("No data collected for bias estimation")
        return np.zeros(3)



gyro_bias = estimate_gyro_bias()

