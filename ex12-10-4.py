#Exercise 12-10-4 - Count # of <p>

import urllib
import re

handler = urllib.urlopen('https://news.google.com/news/?ned=us&hl=en').read()
#p_tags = re.findall('<p.*?', handler)
p_tags = re.findall('</p>', handler)
print len(p_tags)