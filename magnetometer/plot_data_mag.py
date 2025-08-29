import numpy as np
import matplotlib.pyplot as plt

#--------------------FUNCTIONS------------------------#
def load_raw_data(filename):
    raw_data = []
    with open(filename, 'r') as f:
        for line in f:
            mag_x, mag_y, mag_z = map(float, line.strip().split("\t")) #
            raw_data.append([mag_x,mag_y,mag_z])
    return np.array(raw_data)

def calibrate_data(raw_data, bias, A_inv):
    corrected_data = []
    for raw in raw_data:
        corrected = A_inv @ (raw-bias)
        corrected_data.append(corrected)
    return np.array(corrected_data)

#--------------------END_OF_FUNCTIONS------------------------#



INPUT_FILE = "data_text_files/mag_data_for_magneto.txt" # Input file path that contains raw data



bias = np.array([5.345843,-18.711116,-24.588939]) #
A_inv = np.array([[1.367952,-0.015645,0.067976],
                 [-0.015645,1.341725,0.013483],
                 [0.067976,0.013483,1.413720]])

raw_data = load_raw_data(INPUT_FILE)
calibrated_data = calibrate_data(raw_data, bias, A_inv)


#---------------------------------PLOTTING----------------------#


plt.ion()

# Plot XY data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 0], raw_data[:, 1], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 0], calibrated_data[:, 1], 'r*', label='Calibrated Meas.')
plt.title('XY Magnetometer Data')
plt.xlabel('X [µT]')
plt.ylabel('Y [µT]')
plt.legend()
plt.grid()
plt.axis('equal')

# Plot YZ data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 1], raw_data[:, 2], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 1], calibrated_data[:, 2], 'r*', label='Calibrated Meas.')
plt.title('YZ Magnetometer Data')
plt.xlabel('Y [µT]')
plt.ylabel('Z [µT]')
plt.legend()
plt.grid()
plt.axis('equal')

# Plot XZ data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 0], raw_data[:, 2], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 0], calibrated_data[:, 2], 'r*', label='Calibrated Meas.')
plt.title('XZ Magnetometer Data')
plt.xlabel('X [µT]')
plt.ylabel('Z [µT]')
plt.legend()
plt.grid()
plt.axis('equal')

# Plot 3D scatter
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(raw_data[:, 0], raw_data[:, 1], raw_data[:, 2], c='b', marker='*', s=10, label='Raw Meas.')
ax.scatter(calibrated_data[:, 0], calibrated_data[:, 1], calibrated_data[:, 2], c='r', marker='*', s=10, label='Calibrated Meas.')
ax.set_title('3D Scatter Plot of Magnetometer Data')
ax.set_xlabel('X [µT]')
ax.set_ylabel('Y [µT]')
ax.set_zlabel('Z [µT]')
ax.legend()


plt.show()

# Compute and print norms za verifikacijo
raw_norms = np.linalg.norm(raw_data, axis=1)
calibrated_norms = np.linalg.norm(calibrated_data, axis=1)
print(f"Raw data norm - Mean: {np.mean(raw_norms):.2f} µT, Std: {np.std(raw_norms):.2f} µT")
print(f"Calibrated data norm - Mean: {np.mean(calibrated_norms):.2f} µT, Std: {np.std(calibrated_norms):.2f} µT")


input("Press Enter to close all plots...")
plt.close('all')


