import urllib2
from xml.etree import ElementTree

class LiveScore:
    def __init__(self):
        self.scoreUrl = 'http://static.cricinfo.com/rss/livescores.xml' #ref. from quora
        self.filePath = 'livescores.xml' #path to store downloaded xml file
        self.score=''
    def downloadFile(self):
        downloadedFile = urllib2.urlopen(self.scoreUrl)
        with open(self.filePath,'wb') as output:
            output.write(downloadedFile.read())
        #return self
            
    def showScore(self):
        self.score=''
        with open(self.filePath, 'rt') as f:
            tree = ElementTree.parse(f)
            for node in tree.findall('.//channel/item/title'):
                if 'India' in node.text and '/' in node.text: #you can replace team name, in case of IPL :D
                    self.score += node.text + '\n'
        return self.score


prev, new = '',''
score = LiveScore()
while True:
    score.downloadFile()
    new = score.showScore()
    if new != prev : #showing updated score only
        print new
        prev=new
