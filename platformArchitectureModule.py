
#   Below user defined Module contains below methods as

#   CPU_Info_OS()  :    Displays information of CPU depending on OS
#   Platform_Info() :    Displays information of platform(Operating System)
#   Boot_Info() :   Display boot time of Machine
#   CPU_Info()  :   Display all information of CPU
#   RAM_Usage() :   Display Information of RAM Usage
#   Disk_Info() :   Display Information of Hard Disk

import psutil
import platform
from os import *
from datetime import datetime

def CPU_Info_OS():
    print("--------CPU information of OS--------")

    if platform.system() == 'Windows':
        return platform.processor()
    elif platform.system() == 'Darwin':
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return popen(command).read().strip()
    elif platform.system() == 'Linux':
        command = 'cat/proc/cpuinfo'
        return popen(command).read.strip()
    return 'Platform Not Identified'

#################################################################

def get_size(bytes,suffix = "B"):
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor :
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

##############################################################

def Platform_Info():

    print("-----------------System Information---------------")

    uname = platform.uname()
    print(f"System:{uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")





def Boot_Info():
    print("---------------Boot Time information -------------------")

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day}::{bt.hour}-{bt.minute}-{bt.second}")

#################################################################

def CPU_Info():
    print("---------------CPU Info ---------------")
    print("Physical cores",psutil.cpu_count(logical=False))
    print("Total cores",psutil.cpu_count(logical=True))

    cpufreq = psutil.cpu_freq()

    print(f"Max Frequecy : {cpufreq.max:.2f}Mhz")
    print(f"Mix frequency: {cpufreq.min:.2f}Mhz")
    print((f"Current frequency : {cpufreq.current:.2f}Mhz"))

    print("CPU Usage per core")

    for i,percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core{i}:{percentage}%")

    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


def RAM_Usage():
    print("-----------------Memory Usage--------------------")

    svmem = psutil.virtual_memory()

    print(f"Total :{get_size(svmem.total)}")
    print(f"Available :{get_size(svmem.available)}")
    print(f"Used :{get_size(svmem.used)}")
    print(f"Percentage : {svmem.percent}%")
    print("---------SWAP--------------")

    swap = psutil.swap_memory()

    print(f"Total : {get_size(swap.total)}")
    print(f"free : {get_size(swap.free)}")
    print(f"Used : {get_size(swap.used)}")
    print(f"Percentage : {swap.percent}%")


############################################################################

def Disk_Info():
    print("--------------Disk Information")

    partitions = psutil.disk_partitions()

    for partition in partitions :
        print(f"==========Device {partition.device}========")
        print(f"MountPoint : {partition.mountpoint}")
        print(f"File System : {partition.fstype}")
        print(f"Opts : {partition.opts}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"Total Size : {get_size(partition_usage.total)}")
        print(f"Used Size : {get_size(partition_usage.used)}")
        print(f"Free Size : {get_size(partition_usage.free)}")
        print(f"Percentage : {get_size(partition_usage.percent)}%")


    disk_io1 = psutil.disk_io_counters()
    print(f"Total read : {get_size(disk_io1.read_bytes)}")
    print(f"Total Write : {get_size(disk_io1.write_bytes)}")






############################################################################
def main():
    print("inside main")
    # CPU_Inform =   CPU_Info_OS()
   # print(platform.system())
   # print(platform.processor())
    print(CPU_Info_OS())
    #print(CPU_Inform)
    Platform_Info()
    Boot_Info()
    CPU_Info()
    RAM_Usage()
    Disk_Info()
    #disk_io1 = psutil.disk_io_counters()
   # print(f"Total read : {get_size(disk_io1.read_bytes)}")
    #print(f"Total Write : {get_size(disk_io1.write_bytes)}")
    #print(psutil.disk_io_counters())
   # print(psutil.disk_partitions())
################################################################




if __name__ == "__main__":
    main()
