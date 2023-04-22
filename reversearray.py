# using for loop
# arr=[1,2,3,4,5,6,7]
# n=len(arr)
# print(n,'o..')
# rev_arr=[0]*n
# for i in range(n):
#     # print(i,end=' ')
#     rev_arr[n-i-1]=arr[i]
# print(rev_arr)



# using append
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
rev_arr=[]
print('using append')
for i in range((n-1),-1,-1):
    rev_arr.append(arr[i])
print(rev_arr)



# using reverse function
print('using reverse function')
arr=[1,2,3,4,5,6,7,8,9]
rev_arr=list(reversed(arr))
print(rev_arr)

# using slicing function
print('using slicing function')
arr=[1,2,3,4,5,6,7,8,9]
rev_arr=arr[::-1]
print(rev_arr)


# without using extra array
print('without using extra array')
arr=[1,2,3,4,5,6,7,8,9.0]
for i in range(n//2):

    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    print('ll',arr)
