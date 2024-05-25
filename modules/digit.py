def dig(a):
    b=""
    for i in a:
        if a[i].isdigit():
            b=b+int(i)
    print(b)
