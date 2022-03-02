def removeVowel(str):

    returned_str = ""

    for i in str:
        if i not in {"a","e","i","o","u"}:
            returned_str += i

    return returned_str

#print(removeVowel("veribulmacasi"))


def removeVowel2(str):

    return str.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
#print(removeVowel("veribulmacasi"))


def removeVowels3(str):
    vowels = set("aeiou")
    res = []
    for i in str:
        if i not in vowels:
            res.append(i)

    return "".join(res)

print(removeVowel("veribulmacasi"))


def removeVowels(str):

    liste = ["a","e","i","o","u"]

    yeni_str = ""

    for char in liste:
        if char.lower() not in liste:
            yeni_str += char

    return yeni_str

"""
ÇIKARIMLAR:

1) Bir stringi bir 'set' in içine yazarsan o stringin tüm karakterlerini set içinde depolamış olursun

2) lower() methodu string içerisinde bulunan harfleri küçük harfe çevirir.

3) replace() methodu belirlenen bir karakteri veya karakterleri başka bir karakter veya karakterle değiştirir

4) index methodu string içerisindeki belli bir karakterin ilk hangi indexte görüldüğünü söyler
"""










