# Ryan Kelly (rpk2kn)

import urllib.request

link = "http://cs1110.cs.virginia.edu/files/words.txt"
stream = urllib.request.urlopen(link)
words = stream.read().decode("UTF-8").split("\n")
text = input("Type text; enter a blank line to end." + "\n")

while text != '':
    text_words = text.split(" ")
    for word in text_words:
        word = word.strip(""".?!,()"'""")
        if not (word in words or word.lower() in words):
            print("  MISSPELLED:", word)
    text = input()
