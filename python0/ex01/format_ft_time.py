import time
import datetime

# Get the current time since the epoch
t = time.time()

# Format the time
t_in_sec = f"{t:,.4f}"

t_in_scientific = f"{t:.2e}"

# Create DateTime object
date_time_object = datetime.datetime.fromtimestamp(t)

# Format the DateTime object
t_in_date_time = date_time_object.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", t_in_sec, "or", t_in_scientific, "in scientific notation")
print(t_in_date_time)