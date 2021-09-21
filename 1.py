class pola:
    print ("Segitiga")
    n = 5
    for i in range (n):
        for j in range(n, i, -1):
            print ("*",end = "")
        print()
    print ()
    print ("Jajar Genjang")
    n = 5
    i = 1
    a = n
    while (i<=n):
        print (" " * (n-1), "*" * a)
        n = n - 1