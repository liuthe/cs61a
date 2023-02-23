def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    r = 1
    for i in range(k):
        r = r*(n-i)
    return r


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while y//10**i!=0:
        i = i+1
    i=i-1
    yp = y
    s = 0
    for k in range(i):
        di = yp//(10**(i-k))
        s = s + di
        yp = yp - di*(10**(i-k))
    s = s + yp%10
    return s


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n//10**i!=0:
        i = i+1
    i = i-1
    yp = n
    diy = []
    for k in range(i):
        di = yp//10**(i-k)
        diy.append(di)
        yp = yp - di*10**(i-k)
    diy.append(yp%10)
    c = 0
    ad = 0
    for k in range(len(diy)):
        if diy[k]==8:
            c = c+1
            if c>=2:
                ad = ad+1
        else:
            c = 0
    return ad>0