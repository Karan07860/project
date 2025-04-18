def function2(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    
    shorter_length = min(len1, len2)
    return shorter_length

print(function2("karan","Rishika"))