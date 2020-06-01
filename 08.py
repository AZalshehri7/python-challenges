# http://www.pythonchallenge.com/pc/def/integrity.html
# Where is the missing link?
"""
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
"""
# it is encoded using "bzip2"
import bz2

# added b to make it bytes
un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
# when clicking the bee http://www.pythonchallenge.com/pc/return/good.html
# needs login
user = bz2.decompress(un)
password = bz2.decompress(pw)

print(user)
print(password)
# user -> huge
# pass -> file
