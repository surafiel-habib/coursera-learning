from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://py4e-data.dr-chuck.net/comments_1122060.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)