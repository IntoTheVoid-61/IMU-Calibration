# IMU-Calibration Magnetometer

## Description
Data is gathered in units of uT. For information about your local magnetic field strength: [Local Magnetic Field Page](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml#igrfwmm) 




## Steps
1. Create a file (.txt extension) in which you want to store the raw magnetometer values and change the variable OUTPUT_FILE to the name of the file you created. 
   - **Note:** I recommend using relative paths, starting from the directory this script is ran in.

2. Run the get_calibration_data_mag script and follow its instructions
   - When collecting data for the calibration of the magnetometer rotate the IMU in figure 8 shapes.
   

3. Import the collected data into the magneto software and collect the combined bias (b) and the correction for combined scale factors, misalignments and soft iron (A^-1)
   - Follow the instructions in plot_data_mag to visualize and evaluate the results








