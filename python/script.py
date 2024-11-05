sentence = "The quick brown fox jumps over the lazy dog"
dict0 = {}

def count_word_lengths(sentence):
    length = 0
    for i in sentence:
        if i != " ":
            length +=1
        else:
            if length not in dict0:
                   dict0.update({length:1})
            else:
                   count = dict0[length] +1
                   dict0.update({length:count})
            length = 0

    print(dict0)

count_word_lengths(sentence)