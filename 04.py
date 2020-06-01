import urllib.request
import re


number = 12345
pattern = re.compile(r"and the next nothing is (\d+)")

# keep running until break
while True:
    with urllib.request.urlopen(
        f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}"
    ) as response:
        html = str(response.read())
    match = pattern.search(html)
    if match == None:
        # found answer
        print(html)
        break
    # return captured segments in pattern (number)
    number = match.group(1)

    print(number)
