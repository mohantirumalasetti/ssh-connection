import os
import threading

'''
Author : T.Mohan Sri Sai
Summary: This program is developed to connect to the linux distributions in 
local area network through the ssh connection It takes the two inputs [length,series] 
from the user one is mandatory [length]

Dedicated to the MVR COLLEGE students ;)

functions:
ip_gen()  : Generates the list of IPs with in given range
pinging() : Pings the every possible IP in the given range
ssh_connection() : Establishes the ssh connection between the host and the target
'''

ip = []
# "ip" variable stores all ip addresses within given range
length = input("Enter IP Range: ")
series = int(input("Enter IP Series: "))


def ip_gen(max_length, ip_list, s=10):
    # In this function default value of the series is 10 in case we didn't mention any value
    i1 = 1
    while i1 <= max_length:
        ip_str = "192.168." + str(s) + "." + str(i1)
        ip_list.append(ip_str)
        i1 += 1


active = []


# "active" variable stores active hosts

def pinging(all_ip):
    for i2 in all_ip:
        print("Pinging.... {" + str(i2) + "}")
        print("------------------------------------------------------")
        # "ping -c 1 [ip] " is the command to ping target host
        cmd = "ping -c 1 " + i2
        out = os.system(cmd)
        # os.system("") module executes the commands in the system
        if out == 0:
            active.append(i)
        os.system("clear")


def ssh_connect(active_host):
    print("Establishing Connection with {" + str(active_host) + "}")
    # "ssh [ip] -l [username]" is the command to establish connection
    cmd = "'ssh " + str(active_host) + " -l teacher'"
    # "xterm -e 'ssh [ip] -l [username]'" this command opens a new terminal and establishes ssh connection
    st = "xterm -e " + cmd
    os.system(st)


ip_gen(length, ip, series)
pinging(ip)

print("Active Hosts:" + str(len(active)))
print("________________")
for i in active:
    print("{" + str(i) + "}")
print("________________")
for i in active:
    # Here we create the thread for each connection
    t = threading.Thread(target=ssh_connect, args=(i,))
    t.start()

t.join()
# with join() we will join every thread to the single process
print("HAPPY HACKING :)")
# <3
