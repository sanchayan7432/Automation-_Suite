import psutil
import GPUtil
import time
from tabulate import tabulate


def get_cpu_info():

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()

    return {
        "CPU Usage (%)": cpu_usage,
        "CPU Cores": cpu_cores,
        "Max Frequency (MHz)": cpu_freq.max
    }


def get_memory_info():

    mem = psutil.virtual_memory()

    return {
        "Total RAM (GB)": round(mem.total / (1024**3), 2),
        "Used RAM (GB)": round(mem.used / (1024**3), 2),
        "RAM Usage (%)": mem.percent,
        "Available RAM (GB)": round(mem.available / (1024**3), 2)
    }


def get_virtual_memory():

    swap = psutil.swap_memory()

    return {
        "Total Swap (GB)": round(swap.total / (1024**3), 2),
        "Used Swap (GB)": round(swap.used / (1024**3), 2),
        "Swap Usage (%)": swap.percent
    }


def get_gpu_info():

    gpus = GPUtil.getGPUs()

    gpu_data = []

    for gpu in gpus:

        gpu_data.append({
            "GPU Name": gpu.name,
            "Load (%)": round(gpu.load * 100, 2),
            "Memory Used (MB)": gpu.memoryUsed,
            "Memory Total (MB)": gpu.memoryTotal,
            "Temperature (C)": gpu.temperature
        })

    return gpu_data


def get_network_info():

    net = psutil.net_io_counters()

    return {
        "Bytes Sent (MB)": round(net.bytes_sent / (1024**2), 2),
        "Bytes Received (MB)": round(net.bytes_recv / (1024**2), 2)
    }


def get_disk_cache():

    disk = psutil.disk_usage('/')

    return {
        "Disk Total (GB)": round(disk.total / (1024**3), 2),
        "Disk Used (GB)": round(disk.used / (1024**3), 2),
        "Disk Usage (%)": disk.percent
    }


def display_stats():

    cpu = get_cpu_info()
    memory = get_memory_info()
    swap = get_virtual_memory()
    network = get_network_info()
    disk = get_disk_cache()
    gpu = get_gpu_info()

    print("\n===== SYSTEM RESOURCE MONITOR =====\n")

    table = []

    for k, v in cpu.items():
        table.append([k, v])

    for k, v in memory.items():
        table.append([k, v])

    for k, v in swap.items():
        table.append([k, v])

    for k, v in network.items():
        table.append([k, v])

    for k, v in disk.items():
        table.append([k, v])

    print(tabulate(table, headers=["Resource", "Value"], tablefmt="grid"))

    if gpu:

        print("\nGPU Information\n")

        gpu_table = []

        for g in gpu:
            gpu_table.append(list(g.values()))

        print(tabulate(
            gpu_table,
            headers=list(gpu[0].keys()),
            tablefmt="grid"
        ))


def monitor_live():

    while True:

        display_stats()

        print("\nRefreshing in 5 seconds...\n")

        time.sleep(5)


if __name__ == "__main__":

    monitor_live()