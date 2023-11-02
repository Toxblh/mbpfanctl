import os
import sys

sys_dir = "/sys/devices/platform/applesmc.768"

def run_get():
    fan_input = f"{sys_dir}/fan1_input"
    try:
        with open(fan_input, 'r') as file:
            speed = int(file.readline().strip())
            print(speed)
    except FileNotFoundError as fnf_error:
        print("Could not read from {}: {}".format(fan_input, fnf_error), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Unhandled error: {}".format(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_get()