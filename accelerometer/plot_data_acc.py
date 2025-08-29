import numpy as np
import matplotlib.pyplot as plt



"""
    The provided script will serve as a visual reference for the results of the acceleration calibration.
    Ideally the calibrated measurements in the XY, YZ and XZ plane should form a circle,
    with the origin at (0,0) and radius equal to the norm of the gravitational field.

"""

#--------------------FUNCTIONS-----------------------------#
def load_raw_data(filename): # Helper function to load the data from the text file
    raw_data = []
    with open(filename, 'r') as f:
        for line in f:
            acc_x, acc_y, acc_z = map(float, line.strip().split("\t"))
            raw_data.append([acc_x, acc_y, acc_z])
    return np.array(raw_data)

def calibrate_data(raw_data, bias, A_inv): # Calibrates data
    corrected_data = []
    for raw in raw_data:
        corrected = A_inv @ (raw - bias)
        corrected_data.append(corrected)
    return np.array(corrected_data)

#---------------------------------------------------------#

#--------------------INPUTS-----------------------------#

INPUT_FILE = "data_text_files/acc_data_for_magneto.txt" # Path to the data you collected with script from step 1

bias = np.array([-0.037024,-0.018018,-0.004940]) # Change the given values with the values you received from magneto software
A_inv = np.array([[1.085688,-0.040552,0.047971],
                  [-0.040552,1.001181,0.009680],
                  [0.047971,0.009680,0.996338]])

raw_data = load_raw_data(INPUT_FILE)
calibrated_data = calibrate_data(raw_data, bias, A_inv)

#---------------------------------------------------------#




# Plot XY data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 0], raw_data[:, 1], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 0], calibrated_data[:, 1], 'r*', label='Calibrated Meas.')
plt.title('XY Acc Data')
plt.xlabel('X [g]')
plt.ylabel('Y [g]')
plt.legend()
plt.grid()
plt.axis('equal')

# Plot YZ data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 1], raw_data[:, 2], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 1], calibrated_data[:, 2], 'r*', label='Calibrated Meas.')
plt.title('YZ Acc Data')
plt.xlabel('Y [g]')
plt.ylabel('Z [g]')
plt.legend()
plt.grid()
plt.axis('equal')


# Plot XZ data
plt.figure(figsize=(6, 6))
plt.plot(raw_data[:, 0], raw_data[:, 2], 'b*', label='Raw Meas.')
plt.plot(calibrated_data[:, 0], calibrated_data[:, 2], 'r*', label='Calibrated Meas.')
plt.title('XZ Acc Data')
plt.xlabel('X [g]')
plt.ylabel('Z [g]')
plt.legend()
plt.grid()
plt.axis('equal')

# Plot 3D scatter
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(raw_data[:, 0], raw_data[:, 1], raw_data[:, 2], c='b', marker='*', s=10, label='Raw Meas.')
ax.scatter(calibrated_data[:, 0], calibrated_data[:, 1], calibrated_data[:, 2], c='r', marker='*', s=10, label='Calibrated Meas.')
ax.set_title('3D Scatter Plot of Acc Data')
ax.set_xlabel('X [g]')
ax.set_ylabel('Y [g]')
ax.set_zlabel('Z [g]')
ax.legend()

plt.show()

raw_norms = np.linalg.norm(raw_data, axis=1)
calibrated_norms = np.linalg.norm(raw_data, axis=1)
print(f"Raw data norm - Mean: {np.mean(raw_norms):.2f} g, Std: {np.std(raw_norms):.2f} g")
print(f"Calibrated data norm - Mean: {np.mean(calibrated_norms):.2f} g, Std: {np.std(calibrated_norms):.2f} g")



input("Press Enter to close all plots...")
plt.close('all')