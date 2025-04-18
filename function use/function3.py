def function3(word):
    first_letter = word[0]
    last_letter = word[len(word) - 1] #word[-1]
    combined = last_letter + first_letter
    return combined.upper()
print(function3("daphne"))