def words_lengths(phrase):
    return map(lambda word: len(word), [word for word in phrase.split()])
res=list(words_lengths("How long are the words in this phrase"))
print("res-->",res)