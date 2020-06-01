"http://www.pythonchallenge.com/pc/def/ocr.html"
# find rare characters in the mess 02_text.txt
with open("02_text.txt", "r") as f:
    data = f.read()

key = ""

for char in data:

    # ord(chr) returns the ascii value
    # CHECKING FOR UPPER CASE
    if ord(char) >= 65 and ord(char) <= 90:
        key += char
    # checking for lower case
    elif ord(char) >= 97 and ord(char) <= 122:
        key += char

# printing the string which contains only alphabets
print(key)
# key = equality.html
