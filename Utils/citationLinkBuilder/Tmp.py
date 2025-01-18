"""

- https://stackoverflow.com/questions/6191412/how-to-url-encode-periods

"""

import urllib.parse
import re

link = ""
text = ""


with open("link.txt", "r", encoding="utf-8") as f:
    link = f.read()

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

""" V1 ORIGINAL
output = link+"#:~:text="+urllib.parse.quote(text)
"""

#""" V2 ORIGINAL
output = "#:~:text="+urllib.parse.quote(text)
#"""
output = re.sub(r'[.]', r'%2E', output, 0, re.MULTILINE)
#

""" V1 MODIFIED
output = re.sub(output, r"[.]", r"%2E")

"""


with open("output.txt", "w", encoding="utf-8") as f:
    print(output, file=f)


