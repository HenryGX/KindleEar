from HTMLParser import HTMLParser
import urllib2
from apps.dbModels import *

class MyParser(HTMLParser):
    key = None
    reptile = None
    def __init__(self):
        HTMLParser.__init__(self)
        self.f = open(os.path.abspath('/home/ws00381493/htmldataa.txt'), 'w')    

    def __del__(self):
        self.f.close()  
        
    def handle_starttag(self, tag, attrs):
        print >> self.f, "Start tag:", tag
        for attr in attrs:
            print >> self.f, "     attr:", attr
 
    def handle_endtag(self, tag):
        print >> self.f, "End tag  :", tag
    
    def setUserName(self, username):
       self.reptile = ReptileSetup.all().filter('name = ', username).get()

        
if __name__ == '__main__':
    my = MyParser()
    my.setUserName("admin")
    htmlStr = '<!DOCTYPE html><html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'    
    
    url = "https://www.costco.co.jp/search/?text=%E3%83%9E%E3%82%B9%E3%82%AF"
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    htmlStr = response.read()    
                   
    my.feed(htmlStr)