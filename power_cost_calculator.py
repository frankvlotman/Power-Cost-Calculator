import tkinter as tk
from datetime import datetime

def calculate_electricity_cost(start_time, end_time, power_watt, rate_per_kwh):
    """
    Calculate the electricity usage cost.

    :param start_time: Start time in HH:MM format.
    :param end_time: End time in HH:MM format.
    :param power_watt: Power rating of the appliance in watts.
    :param rate_per_kwh: Rate per kWh in pence.
    :return: Total cost in GBP.
    """
    # Convert times to datetime objects
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')

    # Calculate the duration in hours
    duration = (end - start).seconds / 3600

    # Convert power from watts to kilowatts
    power_kw = power_watt / 1000

    # Calculate the total energy consumed in kWh
    energy_used_kwh = power_kw * duration

    # Calculate the cost
    cost = energy_used_kwh * (rate_per_kwh / 100)  # converting pence to pounds

    return cost

def update_end_time(*args):
    end_hour.set(start_hour.get())
    end_minute.set(start_minute.get())

def on_calculate():
    start_time = f"{spin_start_hour.get()}:{spin_start_minute.get()}"
    end_time = f"{spin_end_hour.get()}:{spin_end_minute.get()}"
    power_watt = float(entry_power_watt.get())
    rate_per_kwh = float(entry_rate_per_kwh.get())
    
    cost = calculate_electricity_cost(start_time, end_time, power_watt, rate_per_kwh)
    label_result.config(text=f"The cost of running the appliance is: £{cost:.2f}")

# Create the main window
root = tk.Tk()
root.title("Electricity Cost Calculator")

# Create StringVars for Spinbox values
start_hour = tk.StringVar()
start_minute = tk.StringVar()
end_hour = tk.StringVar()
end_minute = tk.StringVar()

# Set up trace for start time variables
start_hour.trace('w', update_end_time)
start_minute.trace('w', update_end_time)

# Create and place the widgets for start time
tk.Label(root, text="Start Time:").grid(row=0, column=0, padx=10, pady=5)
spin_start_hour = tk.Spinbox(root, from_=0, to=23, width=3, format="%02.0f", textvariable=start_hour)
spin_start_hour.grid(row=0, column=1, padx=5, pady=5)
spin_start_minute = tk.Spinbox(root, from_=0, to=59, width=3, format="%02.0f", textvariable=start_minute)
spin_start_minute.grid(row=0, column=2, padx=5, pady=5)

# Create and place the widgets for end time
tk.Label(root, text="End Time:").grid(row=1, column=0, padx=10, pady=5)
spin_end_hour = tk.Spinbox(root, from_=0, to=23, width=3, format="%02.0f", textvariable=end_hour)
spin_end_hour.grid(row=1, column=1, padx=5, pady=5)
spin_end_minute = tk.Spinbox(root, from_=0, to=59, width=3, format="%02.0f", textvariable=end_minute)
spin_end_minute.grid(row=1, column=2, padx=5, pady=5)

# Create and place the widgets for power and rate
tk.Label(root, text="Power (Watt):").grid(row=2, column=0, padx=10, pady=5)
entry_power_watt = tk.Entry(root)
entry_power_watt.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Rate per kWh (pence):").grid(row=3, column=0, padx=10, pady=5)
entry_rate_per_kwh = tk.Entry(root)
entry_rate_per_kwh.insert(0, "27")
entry_rate_per_kwh.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=on_calculate)
button_calculate.grid(row=4, column=0, columnspan=3, pady=10)

# Create and place the result label
label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
