def isValid(s):
    while '()'in s or '{}' in s or '[]' in s:
        s = s.replace('()' , '').replace('{}','').replace('[]','')

    return s == ''
