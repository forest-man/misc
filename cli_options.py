# Standerd argparse implementation
import argparse
parser = argparse.ArgumentParser(
        description="Hard test ultimate script",
        epilog="Just for future needs")

def cpu_usage():
    print("CPU Usage.")

def mem_usage():
    print("Memory usage")

def disc_usage():
    print("Discspace usage")



# We add some argument name (just name) 
#parser.add_argument("cat1", help="Adding a two", type=int)
#parser.add_argument("cat2", help="Adding a two", type=int)
parser.add_argument("-c","--cpu", help="Consume all CPU", action="store_true")
parser.add_argument("-m","--memory", help="Consume all memory", action="store_true")
parser.add_argument("-d","--disc", help="Consume all discspace", action="store_true")
args = parser.parse_args()
if args.cpu:
    cpu_usage()
elif args.cpu == 1:
    print("Hello")
elif args.cpu == 2:
    print("Goodbye")
elif args.memory:
    mem_usage()
elif args.disc:
    disc_usage()
