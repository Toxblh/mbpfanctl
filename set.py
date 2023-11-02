import os
import sys

sys_dir = "/sys/devices/platform/applesmc.768"
speeds = {"normal": 2000, "medium": 3500, "max": 6000}

def run_set(args):
    if len(args) != 1:
        usage()
        sys.exit(-1)
    param = args[0]
    if param in speeds.keys():
        set_speed(speeds[param])
    else:
        print(f"invalid speed specifier: {param}\n", file=sys.stderr)
        usage()

def usage():
    print("Usage: set [normal|medium|max]")

def set_speed(speed):
    fan_input = f"{sys_dir}/fan1_min"
    try:
        with open(fan_input, 'w') as file:
            file.write(str(speed) + "\n")
    except FileNotFoundError as fnf_error:
        print("Could not write to {}: {}".format(fan_input, fnf_error), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Unhandled error: {}".format(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_set(sys.argv[1:])