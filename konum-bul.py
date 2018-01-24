import os
import sys

try:
	ip = sys.argv[1]
	print "[*] ip :", ip
except:
	print "usage : python konum_bul.py <ip>"
	exit()

print "Lutfen Bekleyiniz.....\n" + "-" * 20
os.system("curl http://api.hackertarget.com/geoip/?q=" + ip )
print ""
