def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if a > b:
        return "First Number Is Greater"
    if b > a:
        return "Second Number Is Greater"
    else:
        return "Numbers Are Equal"