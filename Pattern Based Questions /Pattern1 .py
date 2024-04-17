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
        
