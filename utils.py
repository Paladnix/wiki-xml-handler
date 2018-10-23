#!/usr/bin/env python
# coding=utf-8

import mwparserfromhell
import time

def getInfobox(title, text):
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates(matches='Infobox olympics')

    if len(templates) >= 1:
        print("\n\n\n\n" + title)
        print(templates)
        time.sleep(1)
