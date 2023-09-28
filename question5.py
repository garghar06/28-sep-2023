def filter_words(word_list,letter):
    return filter(lambda word:word[0]==letter,word_list)
li=['hello','are','cat','dog','ham','hi','go','to','heart']
res=filter_words(li,'h')
print("res-->",list(res))