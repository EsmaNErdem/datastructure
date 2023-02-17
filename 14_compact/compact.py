def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = [el for el in lst if el]
    return new_lst

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))