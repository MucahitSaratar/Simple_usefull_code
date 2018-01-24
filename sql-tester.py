import requests
import sys



try:
	url = sys.argv[1]
	istek = url + "'"
	print "istek atiliyor..."
	print istek
	yolla = requests.get(istek)
	kod = yolla.status_code
	print "kontlor ediliyor..."
	if kod != 301 and kod != 404 and kod !=403:
		if  "expects parameter" in yolla.content or "Warning" in yolla.content:
			print "Var :                                                        " + istek
		else:
			print "Yok : " + istek
	else:
		print "Sayfa yok : " + istek
#	print istek

except:
	print "Control-C yapildi..."
