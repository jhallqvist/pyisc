"""
Quick and dirty to scrape data for the different conf files from ISC KB.

So far this is done on locally downloaded html files as I have not yet figured
out how to use BeautifulSoup to correctly get the source code (it seems hidden
in some javascript magic)
"""

from bs4 import BeautifulSoup
import re

html_doc = 'ISC DHCP 4.4 Manual Pages - dhcp-options.html'

soup = BeautifulSoup(open(html_doc))

options = soup.findAll('b', string=re.compile(r'^option.*'))
parents = [x.parent for x in options]

for obj in parents:
    obj.text.replace('\n', ' ')

for option in options:
    option.parent.text.replace('\n', ' ')
