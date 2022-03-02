s=input()
res=""
for x in s:
    if x.isalpha():
        if x.islower():
            res+=chr(ord("a")+ord("z")-ord(x))
        else:
            res += chr(ord("A") + ord("Z") - ord(x))
    else:
        res+=x
print(res)