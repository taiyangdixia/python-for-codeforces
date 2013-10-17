import os  
import urllib2
import urllib
import HTMLParser

url = 'http://10.120.68.1/CCF_contest/Signaling/20121210/10/'
disPath = 'f:\\competition\\'

class MyParser(HTMLParser.HTMLParser):
	filelist = []
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name,value in attrs:
				if name =='href':
					#print value
					if len(value) > 40:
						self.filelist.append(value)
						
					else :
						print "invaild value:%s"%value
	def getfileslist(self):
		return self.filelist
										
if __name__ == '__main__':
	mp = MyParser()	
	web = urllib2.urlopen(url)
	for content in web.readlines():
		mp.feed(content)
	flist = mp.getfileslist()
	for file in flist:
		if not os.path.exists(disPath+file):
			my_url= url+file
			output = disPath + file
			
			urllib.urlretrieve(my_url,output)
			print "end a file:%s"%file
		
		#else:
		#	print "%s is exists"%file
			
	
	
