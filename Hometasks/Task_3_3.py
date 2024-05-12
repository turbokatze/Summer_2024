words = str(input())
words_list = words.split()
longest_word = sorted(words_list, key=len)
print(longest_word[-1])
