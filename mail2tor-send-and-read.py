import socks
import socket
import mechanize as M
import HTMLParser
h = HTMLParser.HTMLParser()

SOCKS_PROXY_HOST = '127.0.0.1'
SOCKS_PROXY_PORT = 9050

creds = ["mail-address","ur-password"]


def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

# add username and password arguments if proxy authentication required.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection



site1 = "http://mail2tor2zyjdctd.onion/squirrelmail/src/login.php"
site2 = "http://mail2tor2zyjdctd.onion/squirrelmail/src/right_main.php"
site3 = "http://mail2tor2zyjdctd.onion/squirrelmail/src/compose.php?mailbox=INBOX&startMessage=1"

br = M.Browser()
br.set_handle_robots(False)
br.addheaders=[("User-agent","Chrome")]
br.set_proxies({"socks5" : "127.0.0.1:9050"})
print "siteye erisim saglaniyor....."
br.open(site1)
br.select_form(nr=0)
br.form["login_username"] = creds[0]
br.form["secretkey"] = creds[1]
print "login olunuyor...."
gonder = br.submit()


def whereismymail(debug="yok"):
	ayar1 =  br.open(site2).read().replace("<tr valign=\"top\">","-"*50).replace("<td align=\"right\">Viewing Messages: <b>1</b> to <b>","-"*50)
	ayar2 = ayar1.split("-"*50)[2:-1]
	ks = []
	if debug == "olsun":
		print "mailler tesipt ediliyor...."
	for i in ayar2:
		kimdengelmis =  i.split("</label>")[0].split(">")[-1]
		subject =  h.unescape(i.split("</a></td>")[0].split(">")[-1])
		ks.append([kimdengelmis,subject])
	if debug == "olsun":
		print "%d kadar mail tesipt edildi....." % (len(ks))
	return ks


def mail_at(kime,konu,icerik,debug="yok"):
	if debug == "olsun":
		print "mail gonderiliyor....."
	br.open(site3)
	br.select_form(nr=0)
	br.find_control("request_mdn").items[0].selected=True
	br.find_control("request_dr").items[0].selected=True
	br.form["mailprio"] = ["1"]
	br.form["send_to"] = "camelloper@mail2tor.com"
	br.form["subject"] = "bu bir python hediyesidir xd"
	br.form["body"] = "burasi da python ile yazilan govde kismi"
	br.submit(name="send")
	if debug == "olsun":
		print "mail atildi..."
