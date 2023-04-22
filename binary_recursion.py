# def binary(n,arr):
#     l=len(arr)
#     left_index=0
#     right_index=l-1
    
#     while right_index>left_index:
#         mid_index=(right_index+left_index)//2
#         midnumber=arr[mid_index]
#         if n==midnumber:
#             print("The number is found at index :",mid_index)
#             return
#         else:
#             if midnumber>n:
#                 right_index=mid_index-1
#             else:
#                 left_index=mid_index+1
#     return "Not found"   



def binary(n,arr,left_index,right_index):
    if right_index>=left_index:
        mid_index=(right_index+left_index)//2
        midnumber=arr[mid_index]
        if n==midnumber:
            print("The number is found at index :",mid_index)
            return
        else:
            if midnumber>n:
                # right_index=mid_index-1
                return binary(n,arr,left_index,mid_index-1)
            else:
                return binary(n,arr,mid_index+1,right_index)

                # left_index=mid_index+1
    return "Not found" 

arr=[1,2,3,4,5,6,7]
value=int(input("Enter your number"))
l=len(arr)
left_index=0
right_index=l-1
re=binary(value,arr,left_index,right_index)
if re:
    print(re)