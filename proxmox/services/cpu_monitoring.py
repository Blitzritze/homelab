#!/usr/bin/env python3
import subprocess
import time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB configuration
token = ""
org = ""
bucket = ""
client = InfluxDBClient(url="http://:8086", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Function for determining the CPU clock rate
def get_cpu_clock_speed():
    cmd = "cat /proc/cpuinfo | grep '^[c]pu MHz' | awk '{print $4}'"
    output = subprocess.check_output(cmd, shell=True).decode('utf-8')
    clock_speeds = output.split()
    return [float(speed) for speed in clock_speeds]

# Function for determining the temperatures
def get_temperatures():
    core_cmds = ["sensors | grep 'Core %d:' | awk '{print $3}' | cut -c2-3" % i for i in range(4)] # 4 = 4 Cores
    package_cmd = "sensors | grep 'Package id 0:' | awk '{print $4}' | cut -c2-3"
    core_temps = [float(subprocess.check_output(cmd, shell=True).decode('utf-8')) for cmd in core_cmds]
    package_temp = float(subprocess.check_output(package_cmd, shell=True).decode('utf-8'))
    return core_temps, package_temp

while True:
    # Retrieve temperatures and CPU clock rates
    core_temps, package_temp = get_temperatures()
    cpu_clock_speeds = get_cpu_clock_speed()

    # Create and write InfluxDB entry
    timestamp = int(time.time() * 1e9)  # Nanoseconds since Epoch
    for i, temp in enumerate(core_temps):
        point = Point("temp") \
            .tag("host", "value") \
            .field(f"core{i}", temp) \
            .time(timestamp, WritePrecision.NS)
        write_api.write(bucket, org, point)
    point = Point("temp") \
        .tag("host", "value") \
        .field("package", package_temp) \
        .time(timestamp, WritePrecision.NS)
    write_api.write(bucket, org, point)

    # Create and write InfluxDB entry for CPU clock rate
    for i, speed in enumerate(cpu_clock_speeds):
        point = Point("cpu_speed") \
            .tag("host", "value") \
            .field(f"cpu{i}", speed) \
            .time(timestamp, WritePrecision.NS)
        write_api.write(bucket, org, point)

    time.sleep(10)  # Wait 10 seconds

