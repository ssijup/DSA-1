
# def recursion(n):
# 	if n==1:
# 		return 0
# 	elif n==2:
# 		return 1
# 	else:
# 		print(n)
# 		return recursion(n-1) + recursion(n-2)
	


# for i in range(5):
# 	print(recursion(i))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def print_fibonacci(n):
#     for i in range(n):
#         print(fibonacci(i), end=' ')

# print_fibonacci(11)





def fibi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        # print(n,end=" ")
        return fibi(n-2)+fibi(n-1)

value=int(input('Enter the number'))
num=fibi(value)
print("Done",num)



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 10
print(f"The {n}th term in the Fibonacci sequence is {fibonacci(n)}")



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    print('90')
    for i in range(n):
        if n<=1:
            return n
        else:
            return         

print_fibonacci(11)