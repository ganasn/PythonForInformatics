#Chapter 12 - Using urllib - Section 12.4 - File Retriever

import urllib

file_handler = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in file_handler:
    print line.strip()