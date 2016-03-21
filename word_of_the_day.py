import os
from bs4 import BeautifulSoup
import urllib2
f=open("Words of day.txt","a")
url= 'http://www.wordthink.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
what=soup.find("h2", {"class": "title"})
word=what.a.contents[0] #Got word
#word='gregarious'
url= 'http://www.wordthink.com/'+word
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
para = soup.find('p').getText()
para = para.encode('ascii',errors='ignore') #removes non ascii characters
print para
notif='notify-send -i /home/varun/Desktop/word.png "'+word+'" "'+str(para)+'"'
f.write(str(para)+"\n\n\n")
#notif='notify-send -i face-glasses "I am wearing glasses"'
os.system(notif)



