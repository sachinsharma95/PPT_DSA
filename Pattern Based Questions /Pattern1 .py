Q1 
****
****
****
****

Solotuin 1 
def pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print()
        

pattern1(4)

QUESTION 2
*
**
***
****

Sol 2 
# n =row 
def pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()


# Q3 1
12
123
1234
12345

Soltion 3 
# n=row
# j column 
def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

Q4
1
22
333
4444
55555

Sol4

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()
        
