# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 01:16:07 2020

@author: Vijay Narsing Chakole

below User Defined module contains below methods as 

CPU_Info_OS : display information of CPU depending on OS
Platform_Info : display information of platform (Operating System)
Boot_Info() : display boot time machine
CPU_Info() : display all information of CPU
RAM_Usage() : display information of RAM usage
Disk_Info() : display information of Hard Disk


    
"""

import psutil
import platform
from os import *
from datetime import datetime

platform.machine()
platform.node()
platform.platform()
platform.processor()
platform.release()

# python related
platform.python_build()
platform.python_compiler()
#platform.python_branch()
platform.python_implementation()
#platform.python_revision()
#platform.python_version()


def Python_Info():
    print("Python information")
    print(f"Python Build : {platform.python_build()}")
    print(f"Python Compiler : {platform.python_compiler()}")
    print(f"Python Implementation : {platform.python_implementation()}")
    

Python_Info()
    
    
    
###############################################################################

def CPU_Info_OS():
    
    if platform.system() == 'Windows':
        return platform.processor()
    elif platform.system() == 'Darwin' :
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return  popen(command).read().strip()
    elif platform.system() == 'Linux':
        command = 'cat/proc/cpuinfo'
        return popen(command).read().strip()
    return 'platform not identified'


#CPU_Info_OS()

###############################################################################

def get_size(bytes, suffix = "B" ):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes<factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

###############################################################################
        
def platform_Info():
    print("Operating System Information")
    uname = platform.uname()
    print(f"System : {uname.system}")
    print(f"Node name : {uname.node}")
    print(f"Release : {uname.release}")
    print(f"Version : {uname.version}")
    print(f"Machine : {uname.machine}")
    print(f"Processor : {uname.processor}")
    
#platform_Info()
    
###############################################################################

def Boot_Info():
    print("Boot Time")
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time YY/MM/DD/H:M:S : {bt.year}/{bt.month}/{bt.day}/{bt.hour}:{bt.minute}:{bt.second}")
    
Boot_Info()

###############################################################################

def CPU_Info():
    print("CPU Information")
    print("Physical core : ", psutil.cpu_count(logical = False))
    print("Total core : ", psutil.cpu_count(logical =  True))
    
    cpufrequency = psutil.cpu_freq()
    print(f"Max frequency : {cpufrequency.max:.2f}MHz")
    print(f"Min frequency : {cpufrequency.min:2f}MHz")
    print(f"Current frequency : {cpufrequency.current}MHz")
    
    print("CPU Usage per Core")
    for i, percentage in enumerate(psutil.cpu_percent(percpu = True)):
        print(f"Core {i} : {percentage}%")
    
    print(f"Total CPU Usage : {psutil.cpu_percent()}%")
    

#CPU_Info()

###############################################################################

"""
To replace pages or segments of data in memory. 
Swapping is a useful technique that enables a computer to execute programs and 
manipulate data files larger than main memory.
The operating system copies as much data as possible into main memory,
and leaves the rest on the disk.

"""

def RAM_Usage():
    print("Memory Information")
    
    sys_virtual_mem = psutil.virtual_memory()
    print(f"Total Memory : {get_size(sys_virtual_mem.total)}")
    print(f"Available Memory : {get_size(sys_virtual_mem.available)}")
    print(f"Used Memory : {get_size(sys_virtual_mem.used)}")
    print(f"Used Memory Percentage : {sys_virtual_mem.percent:.2f}%")
    print(f"Available Memory Percentage : {100 - sys_virtual_mem.percent:.2f}%")

    print("-----------------------------SWAP-------------------")
    
    swap = psutil.swap_memory()    
    print(f"Total Memory : {get_size(swap.total)}")
    print(f"Available Memory : {get_size(swap.free)}")
    print(f"Used Memory : {get_size(swap.used)}")
    print(f"Used Memory Percentage : {swap.percent:.2f}%")
    print(f"Available Memory Percentage : {100 - swap.percent:.2f}%")
        
    
#RAM_Usage()

###############################################################################

def Disk_Info():
    print("Disk Information")
    partitions = psutil.disk_partitions()
    
    for partition in partitions :
         print(f"=== Device : {partition.device} ===")
         print(f"MountPoint : {partition.mountpoint}")
         print(f" File System Type : {partition.fstype}")
         try:
             partition_usage = psutil.disk_usage(partition.mountpoint)
         except PermissionError:
            continue
    
        
         print(f"Total Memory : {get_size(partition_usage.total)}")
         print(f"Available Memory : {get_size(partition_usage.free)}")
         print(f"Used Memory : {get_size(partition_usage.used)}")
         print(f"Used Memory Percentage : {partition_usage.percent:.2f}%")
         print(f"Available Memory Percentage : {100 - partition_usage.percent:.2f}%")   
         
         #disk_io = psutil.disk_io_counters()
        # print(f"Total read : {get_size(disk_io.read_bytes)} ")
        #print(f"Total write : {get_size(disk_io.write_bytes)}")
        
        
#Disk_Info()
     
###############################################################################

# Calling All functions

CPU_Info_OS()
platform_Info()
Boot_Info()
CPU_Info()
RAM_Usage()
Disk_Info() 
Python_Info()

   
