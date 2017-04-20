import urllib
import urllib2
import requests
import json
#url = 'https://world.taobao.com/'
#url = 'https://www.alitrip.com/'
#url='https://www.facebook.com/profile.php?id=100013055412543'
url = 'https://www.baidu.com'

parameters = ''
html = requests.get(url)
print html.text

#url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

#print "downloading with urllib"
#urllib.urlretrieve(url, "code.zip")

#print "downloading with urllib2"
#f = urllib2.urlopen(url)
#data = f.read()
#with open("code2.zip", "wb") as code:
#    code.write(data)

#print "downloading with requests"
#r = requests.get(url)
#with open("code3.zip", "wb") as code:
#    code.write(r.content)