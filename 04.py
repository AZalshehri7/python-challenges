"http://www.pythonchallenge.com/pc/def/linkedlist.php"

import urllib.request
import re


number = 12345
# special cases:
# 16044 divide by two
# 82682 misleading number
pattern = re.compile(r"and the next nothing is (\d+)")

# keep running until break
while True:
    html = (
        urllib.request.urlopen(
            f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}"
        )
        .read()
        .decode()
    )

    match = pattern.search(html)
    if match == None:
        # found answer
        print(html)
        break
    # return captured segments in pattern (number)
    number = match.group(1)

    print(number)

# key = peak.html
