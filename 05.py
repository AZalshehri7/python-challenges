"http://www.pythonchallenge.com/pc/def/peak.html"

"<!-- peak hell sounds familiar ? -->"
import pickle
import urllib.request

raw_data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

data = pickle.load(raw_data)
# print a banner as the file name says
for line in data:
    print("".join([char * num for char, num in line]))

# key = channel
