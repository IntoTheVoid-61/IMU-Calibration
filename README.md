# IMU-Calibration

## Overview
This repository provides a modular framework for the calibration of Inertial Measurement Unit (IMU) sensors. The calibration routines are structured such that each sensor modality can be processed independently:

- **Accelerometer**
- **Gyroscope**
- **Magnetometer**

The provided scripts are designed to:  
- Acquire raw measurements from the IMU in the required format.  
- Store the collected data in `.txt` files.  
- Post-process the data using external calibration software (e.g., *Magneto*, see below).  
- Visualize and evaluate the corrected measurements.  

---

## Calibration Models
The calibration is based on linear sensor models that account for bias and scale/misalignment errors. The corrected measurements are obtained as follows:

### Accelerometer
![equation](https://latex.codecogs.com/svg.image?%5Cmathbf%7Ba%7D_%7Bcal%7D=%5Cmathbf%7BA%7D_%7Bacc%7D%5E%7B-1%7D(%5Cmathbf%7Ba%7D_%7Braw%7D-%5Cmathbf%7Bb%7D_%7Bacc%7D))

### Gyroscope
![equation](https://latex.codecogs.com/svg.image?\boldsymbol{\omega}_{cal}=\boldsymbol{\omega}_{raw}-\mathbf{b}_{gyro})


### Magnetometer
![equation](https://latex.codecogs.com/svg.image?%5Cmathbf%7Bm%7D_%7Bcal%7D=%5Cmathbf%7BA%7D_%7Bmag%7D%5E%7B-1%7D(%5Cmathbf%7Bm%7D_%7Braw%7D-%5Cmathbf%7Bb%7D_%7Bmag%7D))


 

---

## Usage Instructions
1. In the `arduino/` folder, upload the provided sketch to your IMU device using the Arduino IDE.  
   - **Important:** After uploading, close the Arduino IDE to avoid serial port conflicts with the Python scripts.  
2. Follow the specific calibration procedure outlined in each module’s `readme.txt`.  
3. Use the generated data files as input for the *Magneto* calibration software (see link below).  
4. Apply the resulting bias and transformation matrices in your post-processing pipeline using the equations above.
5. For information about your local magnetic field strength: [Local Magnetic Field Page](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml#igrfwmm)
6. For information about your local gravitational field strength: [Local Gravitational Field Page](https://www.sensorsone.com/local-gravity-calculator/) (**Step 6 is not necessary since a good aproximation is 1g** )
    
   

---

## External Calibration Tool
For magnetometer calibration, the repository integrates with the *Magneto* software, available here:  
👉 [Magneto Download Page](https://sailboatinstruments.blogspot.com/2011/09/improved-magnetometer-calibration-part.html)

---

## Units and Conversion
The Arduino firmware outputs measurements in specific engineering units. These are internally converted to SI-compatible units in the Python scripts.  

| Sensor        | Arduino Output | Python Representation        |
|---------------|----------------|-------------------------------|
| Accelerometer | **mg**         | **g** (1 g = 9.80665 m/s²)    |
| Gyroscope     | **DPS (°/s)**  | **rad/s**                     |
| Magnetometer  | **µT**         | **µT**                        |

---
