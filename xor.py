class xorencrypt():
	def __init__(self,key):
		self.key = key


	def code(self,bisey):
		return self.dc(self.xor(self.bn(bisey),self.bn(self.key)))


	def xor(self,text,key):
		dondur2 = ""
		u1 = len(text)
		u2 = len(key)
		fark = u1 - u2
		kosul = fark < 0 or fark > 0
		if kosul and u1 < u2:
			text += "0"*fark
		elif kosul and u2 < u1:
			key += "0"*fark
		for ind in range(len(text)):
			if text[ind] == key[ind]:
				dondur2 += "0"
			else:
				dondur2 += "1"
		return dondur2


	def dc(self,binary):
		dondur3 = ""
		baslangic = 0
		bitis = 8
		for abc in range(len(binary)/8):
			bina = binary[baslangic:bitis]
			kar = chr(int(bina,2))
			dondur3 += kar
			baslangic += 8
			bitis += 8
		return dondur3

	def bn(self,text):
		dondur1 = ""
		for i in text:
			bin1 = bin(ord(i))[2:]
			bin1 = "0"*(8-len(bin1))+bin1
			dondur1 += bin1
		return dondur1
