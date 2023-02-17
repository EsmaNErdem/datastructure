def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # ord() gives numerical corresponding of only lowercaes letter in this case, to find character position, we need to find the difference by referencing a as ("a" = 1, "b" = 2)

    diff = ord('a') - 1

    total = sum((ord(let)-diff) for let in word.lower())

    return not total%2 == 0

print(is_odd_string('amazing'))
print(is_odd_string('AAaa'))
print(is_odd_string('a'))