# Arduino Drive Station App

This application provides a user interface to control an Arduino-based robot through Bluetooth. You can switch between Teleop, Autonomous, Disable and Practice modes using the buttons in the interface. 
The app also displays the status of joystick that connected to computer and you can control the robot using joystick.

![Screenshot_21](https://github.com/user-attachments/assets/12f3c48a-9678-4d8e-aad1-4572efe1e56c)

## Features

- Connect to Bluetooth devices
- Switch between different modes: Teleop, Autonomous, Disable and Practice
- Control the robot using joystick
- Simple and intuitive user interface
- Real-time status updates

## Prerequisites

- Python 3.6 or later
- Tkinter (usually included with Python)
- Pyserial
- Pygame

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/KeremAlperBatal/ArduinoDriveStationApp.git
    cd ArduinoDriveStationApp
    ```

2. **Install the required Python packages:**
    ```sh
    pip install tkinter
    pip install pyserial
    pip install pygame
    ```

## Usage

1. **Run the application:**
    ```sh
    python ArduinoDriveStationAppV2.py
    ```

2. **Interface Description:**
    - **Bluetooth Device Selection:** Select the Bluetooth device you want to connect to from the dropdown list.
    - **Connection Status:** Displays the current connection status.
    - **Mode Buttons:** Three large buttons to switch between Teleop, Autonomous, and Disable modes.
      - Teleop Mode: Green when active, grey when inactive.
      - Autonomous Mode: Green when active, grey when inactive.
      - Disable: Red when active, grey when inactive.
      - Practice Mode: Green when active, grey when inactive.
    - **Joystick Axes and Buttons Values:**  Displays the values of joysticks axes and buttons values in a order (eg. Axes: axis1,axis2,axis3
    Buttons: button1,button2,button3)

3. **Steps to Use:**
    - **Refresh Bluetooth Devices:** Click the "Refresh" button to scan and list available Bluetooth devices.
    - **Select a Device:** Choose a device from the dropdown list and click "Connect."
    - **Switch Modes:** Click one of the mode buttons to switch the robot's mode via Bluetooth.

## Interface Overview

- **Refresh Button:** Scans for available Bluetooth devices.
- **Connect Button:** Connects to the selected Bluetooth device.
- **Mode Buttons:** 
  - **Teleop Mode:** For manual control.
  - **Autonomous Mode:** For autonomous operation.
  - **Disable:** To disable the robot.
  - **Practice Mode:** To test some functions on the robot.

## Example

The following is an example workflow for using the app:

1. Open the application.
2. Click the "Refresh" button to list available Bluetooth devices.
3. Select the appropriate device from the dropdown menu.
4. Click "Connect" to establish a connection.
5. Use the mode buttons to control the robot.

## Arduino Library Integration

This app works with the [Arduino DriveStation Library](https://github.com/KeremAlperBatal/ArduinoDriveStation). Ensure the library is properly integrated into your Arduino project to handle mode changes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact [Kerem Alper Batal](mailto:kerem_batal@hotmail.com).

