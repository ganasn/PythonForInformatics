#Chapter 12 - Section 6 - Hyperlink Collector

import urllib
import re

url = raw_input('Enter URL to scrape>')
handler = urllib.urlopen(url).read()
hyper_links = re.findall('href="(http://.*?)"', handler)
for links in hyper_links:
    print links
#print hyper_links
