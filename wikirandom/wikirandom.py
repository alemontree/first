#!/usr/bin/python

# Finds a random wikipedia page and displays the view count for Dec 2007
import urllib2

response = urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random')
html = response.read()
url = response.geturl()

position = len('http://en.wikipedia.org/wiki/')
name = url[position:]

response = urllib2.urlopen('http://stats.grok.se/en/200712/'+name)

html = response.read()
start = html.find('has been viewed') + 16
end = html.find('times')
count = html[start:end]

print name, count
