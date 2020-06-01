# http://www.pythonchallenge.com/pc/def/map.html


raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# n -> n+2
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")

result = raw.translate(table)

print(result)

# map -> ocr
key = "map"
print(f"------\nhttp://www.pythonchallenge.com/pc/def/{key.translate(table)}.html")

# key = ocr.html
