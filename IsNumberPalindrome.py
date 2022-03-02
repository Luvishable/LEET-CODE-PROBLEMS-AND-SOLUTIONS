# Using String
def isPalindrome1(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]






# By creating new number
def isPalindrome2(x):
    if x < 0:
        return False
    given = x
    newnumber = 0
    while x > 0:
        newnumber = newnumber*10 + x % 10
        x //= 10

    return newnumber == given






# By reversing the seconde half of the number
def isPalindrome3(x):

    if x < 0 or (x > 0 and x % 10 ==0): # negatif sayıları ve rakamları dahil etmiyoruz

        return False
    result = 0
    while x > result:
        result = result * 10 + x % 10
        x //= 10

    return True if (x == result or x == result//10) else False


















