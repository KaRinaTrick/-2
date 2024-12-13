def single_root_words(root_word, *other_word):
    same_words = []
    list_other_word = list(other_word)
    for i in range(len(list_other_word)):
        if root_word.upper() in list_other_word[i].upper() or list_other_word[i].upper() in root_word.upper():
            same_words.append(list_other_word[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
