#!/bin/python3
#geektechstuff

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
print("")
print("Welcome to geektechstuff's chat bot")
print("")
while True:
    print(kernel.respond(input("Type to talk >>> ")))
