import psutil
import GPUtil

def get_cpu():
    return psutil.cpu_percent()

def get_ram():
    mem = psutil.virtual_memory()
    return mem.percent, mem.total, mem.used

def get_swap():
    swap = psutil.swap_memory()
    return swap.percent

def get_network():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def get_gpu():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        return gpu.load * 100, gpu.memoryUsed, gpu.memoryTotal
    return 0, 0, 0