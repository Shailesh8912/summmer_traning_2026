# 1 Nested loops concepts
for i in range (3):
    for j in range (3):
        print(i,j)

# 2 questions loops

for i in range (3):          # * * *
    for j in range (3):      # * * *
        print('*',end=' ')   # * * *
    print()

# 3 Qusetions  tables prints 1 -10
n =int(input("enter a number"))
for i in range (1,n+1):
    for j in range(1,11):
        print(i*j,end=' ')
    print()

#  4 Questions Right triangle
for i in range(1,6):
    for j in range(i):
        print("*",end=' ')
    print()

#  5 Questions ivverted trangle

for i in range(5,0,-1):
    for j in range(i):
        print("#", end=' ')
    print()


   #  6 question Same Number Triangle
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

     # 7 questions Number Triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

 
# 8 questions Floyd's Triangle
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#9  question Alphabet Triangle

for i in range(1, 6):
    ch = 65
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

   #10 Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 11 Prime Numbers (1 to 20)

for i in range(2, 21):
        prime = True 

        for j in range(2, i):
            if i % j == 0:
                prime = False
            break

        if prime:
           print(i)