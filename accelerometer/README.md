# IMU-Calibration Accelerometer

## Description
Data is gathered in units of gs, therefore the norm of the gravitational field in your general location is approximately equal to 1g.
For more accurate applications please consult the information about the magnitude of your local gravitational field: [Local Gravitational Field Page](https://www.sensorsone.com/local-gravity-calculator/)




## Steps
1. Create a file (.txt extension) in which you want to store the raw acceleration values and change the variable OUTPUT_FILE to the name of the file you created. 
   - **Note:** I recommend using relative paths, starting from the directory this script is ran in.

2. Run the get_calibration_data_acc script and follow its instructions
   - When collecting data for the calibration of the accelerometer place it the specified orientation and keep it stationary.
   - When ready to collect data, press "Enter".

3. Import the collected data into the magneto software and collect the combined bias (b) and the correction for combined scale factors, misalignments and soft iron (A^-1)
   - Follow the instructions in plot_data_acc to visualize and evaluate the results








