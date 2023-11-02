import sys
from get import run_get
from set import run_set

speeds = {"normal": 2000, "medium": 3500, "max": 6000}
sys_dir = "/sys/devices/platform/applesmc.768"

def usage():
    print("usage: \n\nAvailable commands:")
    print("\tget\tGet current fan speed")
    print("\tset\tSets minimal fan speed [normal|medium|max]")
    print("\nFor more info on each command, use 'help command'.")
    sys.exit(2)

def print_help(args):
    if len(args) != 1:
        print("usage: help command\n\nToo many arguments given.")
        sys.exit(2)
    arg = args[0]
    if arg == 'get':
        print("\nGet current fan speed")
        print("Usage:\n\tmacfanctl get\n")
    elif arg == 'set':
        print("\nSets minimal fan speed")
        print("Usage:\n\tmacfanctl set [normal|medium|max]\n")
    else:
        print(f"Unknown help topic {arg}. Run 'macfanctl help'.")
        sys.exit(2)

def main(args):
    if len(args) < 1:
        usage()
        return

    command = args[0]
    parameters = args[1:]

    if command == "help":
        print_help(parameters)
        return

    if command == "get":
        run_get()
    elif command == "set":
        run_set(parameters)
    else:
        print(f"Unknown command {command}\n")
        usage()

if __name__ == "__main__":
    main(sys.argv[1:])