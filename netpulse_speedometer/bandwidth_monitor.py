import psutil
import time

class BandwidthMonitor:

    def __init__(self):
        self.last = psutil.net_io_counters()

    def get_speed(self):

        time.sleep(1)

        new = psutil.net_io_counters()

        download = (new.bytes_recv - self.last.bytes_recv) / 1_000_000
        upload = (new.bytes_sent - self.last.bytes_sent) / 1_000_000

        self.last = new

        return round(download,2), round(upload,2)