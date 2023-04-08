text = "hello word of word"
chars_popularity = {x:text.count(text[x]) for x in [x for x in (set(text.split()))]}
words_popularity = {x:text.count(x) for x in [x for x in set(text.split())]}
print(chars_popularity, words_popularity)