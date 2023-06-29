arr1 = [1,2,3,4,5]  # input 
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]



drr=[]
for i in arr1:
    for j in arr2:
        for k in arr3:
            if(i==j and i==k):
                drr.append(i)
                print(drr)  # printig the result



       
