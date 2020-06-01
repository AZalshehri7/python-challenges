# http://www.pythonchallenge.com/pc/def/channel.html

# <!-- <-- zip -->
# <title>now there are pairs</title>

# http://www.pythonchallenge.com/pc/def/channel.zip
# folder 06 is the content
# from readme.txt -> hint1: start from 90052

import zipfile, re


number = 90052

f = zipfile.ZipFile("06_text.zip")
pattern = re.compile(r"Next nothing is (\d+)")

# numbers take us to this -> Collect the comments.
# zip files may have comments
comments = []
while True:
    data = f.read(f"{number}.txt").decode("utf-8")
    print(data)
    match = pattern.search(data)
    if match == None:
        # found answer
        break
    # return captured segments in pattern (number)
    number = match.group(1)
    comments.append(f.getinfo(f"{number}.txt").comment.decode("utf-8"))
print("".join(comments))
# comments = hockey
# hockey.html -> it's in the air. look at the letters.
# key = oxygen
