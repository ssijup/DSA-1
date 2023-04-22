# def binarysearch(num,num_list):
#     rightindex=len(num_list)-1
#     print(type(rightindex))
#     leftindex=0
#     midindex=0
#     while rightindex>=leftindex:
#         midindex=(rightindex+leftindex)//2
#         midnumber=num_list[midindex]
#         if midnumber==num:
#             return midindex
#         if midnumber<num:
#             leftindex=midindex+1
#         else:
#             rightindex=midindex-1

            
#     return -11


# num_list=[1,2,3,4,5,6,7,8,9,0]
# num= int(input('Enter a number'))
# print('op')
# index=binarysearch(num,num_list)
# print(index)




def binarysearch(num_list,num):
    print('pp')
    le=len(num_list)
    rightindex=le-1
    leftindex=0
    midnumber=0

    while rightindex>=leftindex:
        print('okeyy')

        midindex=(leftindex+rightindex)//2
        midnumber=num_list[midindex]
        print(midindex,midnumber)
        if midnumber==num:
            return midindex
        if midnumber>num:
             rightindex=midindex-1
            
        else:
            leftindex=midindex+1
           
    return -1


num=0

num_list=[0,1,2,3,4,5,6,8,9]
oo=binarysearch(num_list,num)
print(oo)

