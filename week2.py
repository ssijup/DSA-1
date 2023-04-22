# def dup(v,strd):
#     for i in v:
#         if i=='A':
#             strd+="*"
#         else :
#             strd+=i
#     return strd



def dup(v,strd):
    new_str={}
    count=0
    for i in v:
        if i in new_str:
            new_str[i]+=1
        else:
            new_str[i]=1
    new_s=""
    for i in v:
        if new_str[i]>1:
            new_s+="-"
        else:
            new_s+=i

    return new_str,new_s


str=str(input("Enter  your word"))
strd=""
result=dup(str,strd)
print(result)