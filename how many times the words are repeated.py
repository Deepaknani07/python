ef word_count(input_string):
    counts = dict()
    words = input_string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('the quick brown fox jumps over the lazy dog'))
