def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiou'
    word = list(s)
    i = 0 
    j =  len(word) - 1

    while i < j:
        if word[i].lower() not in vowels:
            i += 1
        elif word[j].lower() not in vowels:
            j -= 1
        else:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

    return ''.join(word)

print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Hello"))
