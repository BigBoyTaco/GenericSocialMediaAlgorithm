from sys import argv
from data import args

version = "\ndevelopment version: 0.0.1\n"

print(version)
print("use the -h command for help\n")

def start():
    args.checkForPassedArgs(argv)
start()