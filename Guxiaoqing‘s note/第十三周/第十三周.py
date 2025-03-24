import time
import pyclamd
from threading import Thread


class Scan(Thread):
    def __init__(self, IP, scan_type, file):
        Thread.__init__(self)
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP, 3310)
            if cd.ping():
                self.connstr = self.IP + "connection [OK]"
                cd.reload()
                if self.scan_type == "contscan_file":
                    self.scanresult = "{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n".format(cd.multiscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)
            else:
                self.connstr = self.IP + "ping error,exit"
                return
        except Exception as e:
            self.connstr = self.IP + "" + str(e)


IPs = ['127.0.0.1']

scantype = "scan_file"
sanfile = 'D:\\test\\EICAR'

i = 1
threadnum = 2
scanlist = []
for ip in IPs:
    currp = Scan(ip, scantype, sanfile)
    scanlist.append(currp)

    if i % threadnum == 0 or i == len(IPs):
        for task in scanlist:
            task.start()
        for stask in scanlist:
            task.join()
            print(task.connstr)
            print(task.scanresult)

        scanlist = []

    i += 1
