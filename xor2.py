def chrxor(bir,iki):
	return bir ^ iki

def all(metin,skey):
	ret = ""
	key = chrxor(ord(metin[0]),skey)
	ret += chr(key)
#	print "key: ",key
	for ch in metin[1:]:
		key = chrxor(ord(ch),key)
		ret += chr(key)
#		print "key: ",key
	return ret

def coz(metin):
	ret = ""
	metin = metin[::-1]
	for i in range(len(metin)-1):
		ret += chr(chrxor(ord(metin[i]),ord(metin[i+1])))
	return ret[::-1]

#bir = all("+my secret message",66)
#print coz(bir)
#print all("+eger bunu okuyorsan tebrik ederim. cyrpto'n iyiymis. simdi al mu gizli mesaji ne yapiyorsan yap. CRYPTO{CONGATS}",66)
