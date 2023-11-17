from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import subprocess
import re
import time

# InfluxDB connection information
url = "http://:8086"
token = "=="
org = ""
bucket = ""

# List of device paths and associated tags
devices = [
    {
        "device_path": "/dev/pve/vm-501-disk-1",
        "vmid": "501",
        "host": "pJellyfin"
    },
    {
        "device_path": "/dev/pve/vm-502-disk-1",
        "vmid": "502",
        "host": "pDocker"
    },
    {
        "device_path": "/dev/pve/vm-503-disk-0",
        "vmid": "503",
        "host": "pAnsible"
    }
]

# Function for extracting the storage space
def get_remaining_space(device_path):
    try:
        command = f"lvdisplay {device_path}"
        output = subprocess.check_output(command, shell=True, text=True)

        lv_size_match = re.search(r'LV Size\s+(\d+\.\d+)\s+GiB', output)
        mapped_size_match = re.search(r'Mapped size\s+(\d+\.\d+)%', output)

        if lv_size_match and mapped_size_match:
            total_size_gb = float(lv_size_match.group(1))
            used_percent = float(mapped_size_match.group(1))

            # Calculate the remaining size in bytes
            total_size_bytes = total_size_gb * 1024 * 1024 * 1024  # GB to bytes
            remaining_space_bytes = (used_percent / 100) * total_size_bytes

            return remaining_space_bytes
        else:
            print("Error: Information could not be extracted.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error when executing the command: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        return None

# Initialize InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Loop for regular data recording and storage
while True:
    for device in devices:
        device_path = device["device_path"]
        vmid = device["vmid"]
        host = device["host"]

        remaining_space = get_remaining_space(device_path)
        if remaining_space is not None:
            # Create timestamp
            timestamp = int(time.time() * 1e9)  # In nanoseconds

            # Create data point
            point = Point("system") \
                .tag("host", host) \
                .tag("nodename", "proxmoxve") \
                .tag("object", "qemu") \
                .tag("vmid", vmid) \
                .field("disk", remaining_space) \
                .time(timestamp)

            # Write data point to the InfluxDB
            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(bucket, org, point)

    time.sleep(10)  # Repeat every 10 seconds

