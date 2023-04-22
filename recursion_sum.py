#    using normal loop
# def recursionsum(num):
#     total=0
#     for i in range(num+1):
#         total=i+total
#     return total




# USING RECURION IN SUM 
# def recursionsum(num):
#     if num==1:
#         return 1
#     else: 
#         return num + recursionsum(num-1)

def recursionsum(num):
    if num==1:
        return 1
    else: 
       
        return num + recursionsum(num-1)


value=int(input("Enter the number you want to get sum :"))
total=recursionsum(value)
print(total)