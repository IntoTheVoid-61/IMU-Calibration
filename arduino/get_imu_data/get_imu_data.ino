/****************************************************************
 * Simplified_ICM20948_I2C.ino
 * ICM 20948 Arduino Library Demo
 * Stream 9-axis IMU data over I2C
 * Modified for I2C-only usage
 ***************************************************************/
#include "ICM_20948.h" // Library: http://librarymanager/All#SparkFun_ICM_20948_IMU

#define SERIAL_PORT Serial
#define WIRE_PORT Wire // I2C port (e.g., Wire on most Arduino boards)
#define AD0_VAL 0      // I2C address bit (0 if ADR jumper closed, 1 otherwise)

ICM_20948_I2C myICM; // I2C object for ICM-20948

void setup()
{
  SERIAL_PORT.begin(115200); // Start serial at 115200 baud
  while (!SERIAL_PORT) { };  // Wait for serial to initialize

  WIRE_PORT.begin();         // Initialize I2C
  WIRE_PORT.setClock(50000); // Set I2C speed to 400kHz

  myICM.enableDebugging(); // Uncomment to enable debug messages

  bool initialized = false;
  while (!initialized)
  {
    myICM.begin(WIRE_PORT, AD0_VAL); // Start sensor with I2C port and address bit

    SERIAL_PORT.print(F("Initialization of the sensor returned: "));
    SERIAL_PORT.println(myICM.statusString());
    if (myICM.status != ICM_20948_Stat_Ok)
    {
      SERIAL_PORT.println("Trying again...");
      delay(500);
    }
    else
    {
      initialized = true;
    }
  }
}

void loop()
{
  if (myICM.dataReady()) // Check if sensor data is ready
  {
    myICM.getAGMT();       // Get acceleration, gyro, mag, and temp data
    printScaledAGMT(&myICM); // Print scaled values
    delay(30);             // Small delay between readings
  }
  else
  {
    SERIAL_PORT.println("Waiting for data");
    delay(500);            // Wait before checking again
  }
}

// Helper function to format floating-point numbers
void printFormattedFloat(float val, uint8_t leading, uint8_t decimals)
{
  float aval = abs(val);
  if (val < 0) SERIAL_PORT.print("-");
  else SERIAL_PORT.print(" ");
  
  for (uint8_t i = 0; i < leading; i++)
  {
    uint32_t tenpow = (i < leading - 1) ? 1 : 0;
    for (uint8_t c = 0; c < leading - 1 - i; c++) tenpow *= 10;
    if (aval < tenpow) SERIAL_PORT.print("0");
    else break;
  }
  SERIAL_PORT.print(val < 0 ? -val : val, decimals);
}

// Print scaled sensor data
void printScaledAGMT(ICM_20948_I2C *sensor)
{
  SERIAL_PORT.print("Scaled. Acc (mg) [ ");
  printFormattedFloat(sensor->accX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accZ(), 5, 2);
  SERIAL_PORT.print(" ], Gyr (DPS) [ ");
  printFormattedFloat(sensor->gyrX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrZ(), 5, 2);
  SERIAL_PORT.print(" ], Mag (uT) [ ");
  printFormattedFloat(sensor->magX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magZ(), 5, 2);
  SERIAL_PORT.print(" ], Tmp (C) [ ");
  printFormattedFloat(sensor->temp(), 5, 2);
  SERIAL_PORT.print(" ]");
  SERIAL_PORT.println();
}