# find longest word in sentence

sentence = "i am learning data science with python"

sentence_list = sentence.split(" ")
longest_word = sentence_list[0]
for word in sentence_list:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)