# coding=utf-8
import urllib.request
import random
import re
useragents=["AdsBot-Google ( http://www.google.com/adsbot.html)",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)"
]

def proxyget(url):
	try:
		req = urllib.request.Request(url) 
		req.add_header("User-Agent", random.choice(useragents)) 
		sourcecode = urllib.request.urlopen(req, timeout = 10) 
		for line in sourcecode :
				ip = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", str(line)) 
				ipf = list(filter(lambda x: x if not x.startswith("0.") else None, ip)) 
				if ipf: 
					for x in ipf:						
						out_file = open("proxy.txt","a")
						while True:
							out_file.write(x+"\n") 
							out_file.close()
							break 
	except:
		print("\nAn error occurred, skipping to the next website.")



def proxylist(): 
	global proxies
	print ("\nChecking for duplicates...")
	proxies = open("proxy.txt").readlines() 
	proxiesp = []
	for i in proxies:
		if i not in proxiesp:
			proxiesp.append(i) 
	filepr = open("proxy.txt", "w") 
	filepr.close()
	filepr = open("proxy.txt", "a") 
	for i in proxiesp:
		filepr.write(i)
	print("Current IPs in proxylist: %s" % (len(open("proxy.txt").readlines())))
	print ("\nProxylist Updated!\n")

def get_proxy():
	out_file = open("proxy.txt","w") 
	out_file.close()
	foxtools = ['http://api.foxtools.ru/v2/Proxy.txt?page=%d' % n for n in range(1, 6)]
	for position, url in enumerate(foxtools):
		proxyget(url)
	print("Current IPs in proxylist: %s" % (len(open("proxy.txt").readlines())))

if __name__ == '__main__':
	get_proxy()