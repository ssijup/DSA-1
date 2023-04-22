# def linerre(n,l):
#     for i in range(l) :
#         if n in arr:
#             return "the number is found"
#     return "not found"
     

def linerre(n,l):
    if l<0:
        return "The number not found"
    elif n==arr[l]:
        return "The number found in the array"
    else:
        c=0
        # print(l,"l",c,end="")
        ++c
        return linerre(n,l-1)



arr=[1,2,3,4,5,6]
ll=len(arr)
l=ll-1
value = int(input("Enter you number"))
result=linerre(value,l)
print(result)