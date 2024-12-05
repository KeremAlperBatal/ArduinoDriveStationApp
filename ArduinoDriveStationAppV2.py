import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import pygame
import threading
import time
import json

# Initialize the joystick
pygame.init()
pygame.joystick.init()

# Variables for serial communication
ser = None
connected = False

# Active mode
active_mode = 'Disable'

# Function to read joystick inputs
def read_joystick():
    """
    Continuously read joystick data and send it to the serial port in JSON format.
    Updates GUI with the latest joystick values.
    """
    global connected
    while connected:
        pygame.event.pump()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        
        # Get axes and button data
        axes = [round(joystick.get_axis(i), 2) for i in range(joystick.get_numaxes())]
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
        
        # Send data to the serial port
        if ser and connected:
            if active_mode:
                mode_data = {"mode": active_mode}
                ser.write(json.dumps(mode_data).encode() + b'\n')
            
            axes_data = {"axes": axes}
            ser.write(json.dumps(axes_data).encode() + b'\n')
            
            buttons_data = {"buttons": buttons}
            ser.write(json.dumps(buttons_data).encode() + b'\n')
        
        # Update GUI with joystick data
        axes_display.set(f"Axes: {', '.join(map(str, axes))}")
        buttons_display.set(f"Buttons: {', '.join(map(str, buttons))}")
        
        time.sleep(0.1)

# Refresh the list of available COM ports
def refresh_ports():
    """
    Refresh the list of available serial ports and update the dropdown menu.
    """
    ports = serial.tools.list_ports.comports()
    port_list = [port.device for port in ports]
    combo['values'] = port_list

# Connect to the selected COM port
def connect():
    """
    Establish a serial connection with the selected COM port.
    """
    global ser, connected
    selected_port = combo.get()
    if selected_port:
        ser = serial.Serial(selected_port, 9600)
        connected = True
        threading.Thread(target=read_joystick, daemon=True).start()
        status_label.config(text="Connected", fg="green")

# Refresh button action
def refresh():
    """
    Trigger the refresh_ports function when the refresh button is clicked.
    """
    refresh_ports()

# Functions to handle mode selection
def teleop():
    """
    Set the active mode to 'Teleop' and update button colors.
    """
    global active_mode
    active_mode = 'Teleop'
    update_button_colors(teleop_button)

def autonomous():
    """
    Set the active mode to 'Autonomous' and update button colors.
    """
    global active_mode
    active_mode = 'Autonom'
    update_button_colors(autonomous_button)

def disable():
    """
    Set the active mode to 'Disable' and update button colors.
    """
    global active_mode
    active_mode = 'Disable'
    update_button_colors(disable_button, is_disable=True)

def practice():
    """
    Set the active mode to 'Practice' and update button colors.
    """
    global active_mode
    active_mode = 'Practice'
    update_button_colors(practice_button)

# Update the button colors based on the selected mode
def update_button_colors(active_button, is_disable=False):
    """
    Highlight the active mode button and reset others.
    """
    buttons = [teleop_button, autonomous_button, disable_button, practice_button]
    for button in buttons:
        if button == active_button:
            button.config(bg="red" if is_disable else "green")
        else:
            button.config(bg="grey")

# Create the GUI
root = tk.Tk()
root.title("Arduino Drive Station App")

# Frame for Bluetooth connection
frame_bt = ttk.LabelFrame(root, text="Bluetooth Connection")
frame_bt.pack(padx=10, pady=10, fill="x")

# Dropdown for Bluetooth devices
combo = ttk.Combobox(frame_bt, state="readonly")
combo.pack(side="left", padx=5, pady=5)

# Button to refresh the list of Bluetooth devices
refresh_button = ttk.Button(frame_bt, text="Refresh", command=refresh)
refresh_button.pack(side="left", padx=5, pady=5)

# Button to connect to the selected Bluetooth device
connect_button = ttk.Button(frame_bt, text="Connect", command=connect)
connect_button.pack(side="left", padx=5, pady=5)

# Frame for mode selection buttons
frame_modes = ttk.LabelFrame(root, text="Modes")
frame_modes.pack(padx=10, pady=10, fill="x")

# Mode buttons
teleop_button = tk.Button(frame_modes, text="Teleop Mode", bg="grey", fg="white", command=teleop)
teleop_button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

autonomous_button = tk.Button(frame_modes, text="Autonomous Mode", bg="grey", fg="white", command=autonomous)
autonomous_button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

disable_button = tk.Button(frame_modes, text="Disable", bg="grey", fg="white", command=disable)
disable_button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

practice_button = tk.Button(frame_modes, text="Practice Mode", bg="grey", fg="white", command=practice)
practice_button.pack(side="left", padx=10, pady=10, fill="x", expand=True)

# Labels to display joystick data
axes_display = tk.StringVar()
buttons_display = tk.StringVar()

axes_label = tk.Label(root, textvariable=axes_display)
axes_label.pack(pady=5)

buttons_label = tk.Label(root, textvariable=buttons_display)
buttons_label.pack(pady=5)

# Label to display connection status
status_label = tk.Label(frame_bt, text="Not Connected", fg="red")
status_label.pack(side="left", padx=5, pady=5)

# Start the main GUI loop
root.mainloop()
