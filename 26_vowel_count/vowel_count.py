def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    dict = {}
    for vowel in phrase:
        if vowel in "aeiou":
            dict[vowel] = dict.get(vowel , 0) + 1

    return dict

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!') )
