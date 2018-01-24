
try:
	import hashlib
	import sys
except:
	print "Module Not Found.!"
	exit()
try:
	text = sys.argv[1]
	sifre = hashlib.md5(text).hexdigest()
	m = "Original :{}\nMd5      :{}".format(text, sifre)
	print m
except:
	print "usage : pytohn md5.py <text>"
