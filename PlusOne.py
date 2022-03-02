"""
We are given a list of integers. We add 1 then return result:

[1,2,3] --> [1,2,4] 123+1=124
"""

def PlusOne(liste):

    n = len(liste)

    for i in range(n):

        index = n-1-i

        # eğer current index zero 9 ise set it to 0.
        if liste[index] == 9:
            liste[index] = 0

        # eğer o anki index 9 değilse
        else:
            liste[index] += 1
            return liste

    # eğer buraya kadar geldiysek sayıdaki tüm basamaklar 9'lardan oluşuyor demektir
    return [1] + liste