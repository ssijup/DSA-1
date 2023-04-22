# a=[1,2,3,4,5,6]
# b=[6,5,4,3,2,1,]
# n=len(a)

# for i in range(n//2):
#     a[i],a[n-i-1]=a[n-i-1],a[i]
# print(a)
# if a==b:
#     print('ok')
# else :
#     print('Not')

# a=input('Enter Your Numbers')
# # b=[6,5,4,3,2,1,]
# n=len(a)
# flag=0
# for i in range(n):
#     if a[i]==a[n-i-1]:
#        flag=1
#     else:
#         flag=2
#         break
#         # print('Its not')
# if flag==1:
#     print('Its palindrome')
# else :
#     print('Its not ')



string=input('Enter your word :')
is_string=True
for i in range(len(string)//2):
    if string[i] != string[len(string)-i-1]:
        is_string=False
        break
if is_string==True:
    print('Its palindrome')
else:
    print('Its not')