def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


def gcd(a, b):
    r = a%b
    print (r)
    if r == 0:
        print("gcd = " + str(b))
        return b
    else:
        gcd(b,r)


# comparing recursively by character in each string
def compareTo(s1, s2):
    string1 = True
    string2 = True
    try:
        s1[0]
    except:
        string1 = False
    try:
        s2[0]
    except:
        string2 = False

    if string1 == True and string2 == True:
        compareTo(s1[1:],s2[1:])

    elif string1 == False and string2 == True:
        print("String 2 longer")
        return -1
    elif string1 == True and string2 == False:
        print("String 1 Longer")
        return 1
    else:
        print("Strings same length")
        return 0