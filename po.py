# def refac(n):
#     j=0
#     for i in range(n):
        
#         return refac(i(i+j))

# print(refac(5))


# a="MALAYALAM"
b='A'
# l=len(a)


def find(a):
    seen=set()
    result=""
    for i in a:
        if 'A' == i:
            result+='*'
        else:
            print('oo')
            result+=i
            # a.add(i)
    return result
            

asp=find("MALAYALAM")
print(asp)