# Week 6
# URLLIB

# working with urllib

# Try getting this website: https://huntersrunstables.com/about

# Choose a website and try to get the web page using urllib. If it doesn't return a page (perhaps because it uses 
# cookies or other interactions to actually return content), try another one.
#
# Use BeautifulSoup to parse the document and choose some tags to obtain. You can do something simple like get the
# href attribute of all the anchor tags. Please submit your code and output, but please print only a small amount, for example, the first 10 tags. Or you may choose to find some other content from the html page.

# After you have posted your response, check out what some of your classmates have done.

import urllib.request

# get request from URL
newweb = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'
# parse with BeautifulSoup
from bs4 import BeautifulSoup

with urllib.request.urlopen(newweb) as f:
    contents = f.read()
    
    soup = BeautifulSoup(contents, 'html.parser')
    
    print("--------------------------Head-----------------------------")
    print(soup.head)
    print("--------------------------href-----------------------------")
    print(soup.href)
    print("--------------------------li (list)-----------------------------")
    print(soup.li)
    print("--------------------------p (paragraph)-----------------------------")
    print(soup.p)
    
# Find some websites that give RSS feeds, noting that some use the XML given in the ATOM specification. 
# Then choose one and use urllib.request to get the document.
#
# Use ElementTree to parse the document and choose some tags to obtain. You can do something simple like get the title tags. 
# Please submit your code and your output, but please print only a small amount, for example the first 10 tags. 
# Or you may choose to find some other content from the xml document.
#
# Once you have submitted your code and results, look at those of two or three of your fellow classmates to see what they did.
    
rss1 = 'http://feeds.bbci.co.uk/news/world/rss.xml'
rss2 = 'http://rss.cnn.com/rss/edition_world.rss'
rss3 = 'https://www.yahoo.com/news/world/rss'

import urllib.request

xmlstring = urllib.request.urlopen(rss1).read().decode('utf8')
len(xmlstring)

xmlstring[:500]

import xml.etree.ElementTree as etree
import io

xmlfile = io.StringIO(xmlstring)
tree = etree.parse(xmlfile)
type(tree)

root = tree.getroot()
type(root)

root.tag
root.attrib
root.text
len(root)

for child in root:
    print(child)
    
firstchild = root[0]
type(firstchild)

firstchild.tag
firstchild.attrib
firstchild.text
len(firstchild)

firstgrandchild = firstchild[0]
firstgrandchild.tag
firstgrandchild.attrib
firstgrandchild.text
len(firstgrandchild)

itemlist = firstchild.findall('item')
len(itemlist)
firstitem = itemlist[0]
firstitem.attrib
firstitem.text
len(firstitem)

for element in firstitem:
    print(element.tag, element.attrib, element.text)
    
firstitem = firstchild.find('item')
firstitem

alltitles = tree.findall('.//title')
len(alltitles)
for title in alltitles[:6]:
    print(title.text)
