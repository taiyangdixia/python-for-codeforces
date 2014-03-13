import sys
import urllib2
import BeautifulSoup
import re
from Queue import Queue
import string
reload(sys)
sys.setdefaultencoding('utf-8')


class MyParser :
	finishedqueue = []
	def __init__(self,seedqueue,reurl,path):
		self.reurl = reurl
		
		self.seedqueue = seedqueue
		self.path = path
	
	def run(self):
		
		while len(self.seedqueue) > 0 :
			pageurl = self.seedqueue.pop(0)
			if pageurl not in self.finishedqueue:
				self.finishedqueue.append(pageurl)
				contentPage = urllib2.urlopen(pageurl).read().decode('gbk')
				#print contentPage
				pagesoup = BeautifulSoup.BeautifulSoup(contentPage)
				self.writeTextToFile(pageurl,pagesoup)
				self.extractNewUrl(pagesoup)
	def writeTextToFile(self,pageurl,pagesoup):
		#print "enter the writeTextToFile"
		#print pagesoup
		tags = pagesoup.findAll('div',attrs={'id':"Cnt-Main-Article-QQ"})
		
		
		print "the len is %d"%len(tags)
		if len(tags) > 0:
			contents = tags[0].contents
			strlist = pageurl.split('/')
			#print contents
			filename = strlist[-2]+strlist[-1]
			filename = filename.split('.')[0]+'.txt'
			#print "path is :%s"%self.path
			record = open(self.path+filename,'w')
			
			contentstr =u''
			for eachstr in contents:
				if isinstance(eachstr,BeautifulSoup.Tag):
				#if eachstr.__class__== <class 'BeautifulSoup.Tag'>:
					if eachstr.name == 'p' and eachstr.string != None :
						contentstr = contentstr + eachstr.string
						
						
			record.write(contentstr.encode('utf-8'))
						
			record.close()
	def extractNewUrl(self,seedpagesoup):
		
		tags = seedpagesoup.findAll('a')
		
		for eachtag in tags :
			if eachtag.has_key('href'):
				#print "find a tag :%s"%eachtag
				urlstr = eachtag['href']
				
				if urlstr not in self.seedqueue:
					m = re.match(self.reurl,urlstr)
					
					if m is not None:
						print "new urlstr is %s"%urlstr
						self.seedqueue.append(urlstr)
						

					
def run():
	
	print "program runs!"
	seadurl = "http://finance.qq.com/"
	reurl = seadurl+'[a-z]+/[0-9]+/[0-9]+\.htm'
	path = "e:\\test\\"
	seedqueue = []
	seedqueue.append(seadurl)
	parser = MyParser(seedqueue,reurl,path)
	parser.run()
	print "program end!"
if __name__ == '__main__':
	run()
	
	
