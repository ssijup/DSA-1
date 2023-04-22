# def unique(arr):
#     l=len(arr)
#     count={}
   
#     for i in arr:
#         if i in arr:
#             count[i]+=1
#         else:
#             count[i]==1
#     for i in arr:
#         if count[i]==1:
#             print("The element is unique",i)

           
# arr=[1,2,3,3,4,4,5]
# unique(arr)



def binarysearch(n,arr):
    l=len(arr)
    midnumber=None
    leftindex=0
    rightindex=l-1

    while rightindex>=leftindex:
        midindex=(leftindex+rightindex)//2
        midnumber=arr[midindex]

        if midnumber==n:
            print("The number is found at the index :",midnumber)
            break
        else:
            if midnumber>n:
                rightindex=midindex-1
            else:
                leftindex=midindex+1
 



arr=[1,2,3,4,5,6,7]
n=5
binarysearch(n,arr)