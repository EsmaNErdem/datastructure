def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # words = phrase.split()
    # words[0] = words[0].capitalize()
    # return " ".join(words)
    return phrase.capitalize()


print(capitalize('only first word'))
print(capitalize('python'))
