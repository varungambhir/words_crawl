import os
from bs4 import BeautifulSoup
import urllib2
import random
f=open("quizlet.txt","a")
url= 'https://quizlet.com/94632828/nytimes-flash-cards/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
what= soup.find_all('span', attrs={'class':'TermText qWord lang-en'})
what1=soup.find_all('span', attrs={'class':'TermText qDef lang-en'})

#for i in range (len(what)):
#	print str(what[i].contents[0])+" "+str(what1[i].contents[0])

x=random.randint(0,len(what)-1)


notif='notify-send -i /home/varun/Desktop/word.png "'+str(what[x].contents[0])+'" "'+str(what1[x].contents[0])+'"' #change path for image accordingly

f.write(str(what[x].contents[0])+"->"+str(what1[x].contents[0])+"\n\n")

os.system(notif)






