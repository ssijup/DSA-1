def linearsearch(num,num_list):
    for num_pos,element in enumerate(num_list):
        if num == element:
            print('we found the element',element,' at the index',num_pos)
            return num_pos
        
    return -1
            


num_list=[1,2,3,4,5,6,7,8,9,0,23]
num=int(input('Enter a number'))
print('op')
index=linearsearch(num,num_list)
print(index)
    
    