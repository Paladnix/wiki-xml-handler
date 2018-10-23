import xml.sax
from utils import *

class WikiXmlHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._pages = []


    def characters(self, content):
        if self._current_tag:
            self._buffer.append(content)


    def startElement(self, name, attrs):
        if name in ('title', 'text'):
            self._current_tag = name
            self._buffer = []


    def endElement(self, name):
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            # self._pages.append((self._values['title'], self._values['text']))
            getInfobox(self._values['title'], self._values['text']);


