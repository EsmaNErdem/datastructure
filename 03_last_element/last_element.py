def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    "[] is a falsy value"
    if lst:
        return lst[-1]

print("List:", list(range(10)), "Last El:", last_element(list(range(10))))