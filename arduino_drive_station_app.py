import tkinter as tk
from tkinter import ttk, messagebox
import serial.tools.list_ports

class ArduinoDriveStationApp:
    def __init__(self, root):
        # Initialize the application
        self.root = root
        self.root.title("Arduino Drive Station")
        self.serial_connection = None

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Create frame for Bluetooth connection
        frame_bt = ttk.LabelFrame(self.root, text="Bluetooth Connection")
        frame_bt.pack(padx=10, pady=10, fill="x")

        # Dropdown list for Bluetooth devices
        self.bt_devices = ttk.Combobox(frame_bt, state="readonly")
        self.bt_devices.pack(side="left", padx=5, pady=5)

        # Label to display connection status
        self.bt_status = ttk.Label(frame_bt, text="Not Connected")
        self.bt_status.pack(side="left", padx=5, pady=5)

        # Button to refresh Bluetooth devices
        self.bt_refresh_btn = ttk.Button(frame_bt, text="Refresh", command=self.refresh_bt_devices)
        self.bt_refresh_btn.pack(side="left", padx=5, pady=5)

        # Button to connect to selected Bluetooth device
        self.bt_connect_btn = ttk.Button(frame_bt, text="Connect", command=self.connect_bt)
        self.bt_connect_btn.pack(side="left", padx=5, pady=5)

        # Create frame for mode buttons
        frame_modes = ttk.LabelFrame(self.root, text="Modes")
        frame_modes.pack(padx=10, pady=10, fill="x")

        # Buttons for different modes
        self.btn_teleop = tk.Button(frame_modes, text="Teleop Mode", bg="grey", fg="white", command=lambda: self.set_mode('T'))
        self.btn_teleop.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.btn_autonom = tk.Button(frame_modes, text="Autonom Mode", bg="grey", fg="white", command=lambda: self.set_mode('A'))
        self.btn_autonom.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.btn_disable = tk.Button(frame_modes, text="Disable", bg="grey", fg="white", command=lambda: self.set_mode('D'))
        self.btn_disable.pack(side="left", padx=10, pady=10, fill="x", expand=True)

    # Function to refresh the list of Bluetooth devices
    def refresh_bt_devices(self):
        ports = serial.tools.list_ports.comports()
        self.bt_devices['values'] = [port.device for port in ports]

    # Function to connect to the selected Bluetooth device
    def connect_bt(self):
        selected_port = self.bt_devices.get()
        if not selected_port:
            messagebox.showwarning("Warning", "Please select a Bluetooth device")
            return

        try:
            self.serial_connection = serial.Serial(selected_port, 9600)
            self.bt_status.config(text="Connected")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect: {e}")
            self.bt_status.config(text="Not Connected")

    # Function to set the mode of the robot
    def set_mode(self, mode):
        if not self.serial_connection or not self.serial_connection.is_open:
            messagebox.showwarning("Warning", "No Bluetooth device connected")
            return

        try:
            self.serial_connection.write(mode.encode())
            self.update_button_colors(mode)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send mode: {e}")

    # Function to update the colors of mode buttons
    def update_button_colors(self, active_mode):
        self.btn_teleop.config(bg="grey" if active_mode != 'T' else "green")
        self.btn_autonom.config(bg="grey" if active_mode != 'A' else "green")
        self.btn_disable.config(bg="grey" if active_mode != 'D' else "red")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoDriveStationApp(root)
    root.mainloop()
