def pattern(n):
    for i in range(0,n,1):
        #Pring leading spaces
        for j in range(0,(n-i)-1,1):
            print(" ", end='')
        for j in range(0,i, 1):
            print(i+j, end='')
        for j in range(i-2,-1,-1):
            print(i+j, end='')
        for j in range(0,(n-i)-1,1):
            print(" ", end='')

        print()

pattern(5)