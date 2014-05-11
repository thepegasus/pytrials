#!/usr/bin/python3
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", str(tag))
    def handle_endtag(self, tag):
        print("Encountered an end tag :", str(tag))
    def handle_data(self, data):
        print("Encountered some data  :", str(data))

htmlData="""<html><body><h1>It works!</h1>
<p>This is the default web page for this server.</p>
<p>The web server software is running but no content has been added, yet.</p>
</body></html>
"""
parser = MyHTMLParser()
parser.feed(str(htmlData))