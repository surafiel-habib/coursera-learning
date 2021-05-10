import json
from urllib.request import urlopen
sum = 0

url = "http://py4e-data.dr-chuck.net/comments_1122063.json"
print ("retrieving URL .............")
fi = urlopen(url)
data= fi.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	sum = sum + number
print (sum)