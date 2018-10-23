#!/usr/bin/env python
# coding=utf-8

import xml.sax
import logging

from WikiXmlHandler import *
import mwparserfromhell

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)


def getInfobox(text):
    wikicode = mwparserfromhell.parser(text)
    template = wikicode.filter_templates('Infobox')


def main():
    handler = WikiXmlHandler()

    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    logging.info("running... ")

    with open('../data/zhwiki-latest-pages-articles.xml', 'r') as fin :
        for line in fin:
            parser.feed(line)

            if len(handler._pages) > 200:
                break
    
    print(handler._pages[19])

if __name__ == '__main__':
    main()
