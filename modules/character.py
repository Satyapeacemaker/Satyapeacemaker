def chara(a):
    b=""
    for i in a:
        if (ord(i)>=65 and ord(i)<=90):
            b=b+chr(ord(i)+32)
        else:
            b=b+i
    print(b)
