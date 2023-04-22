# All cup are opened
def recrusion(n):
    if n==1:
        print('the cups are opened ')
        return 'u'
    print(n)
    return recrusion(n-1)
    

recrusion(5)
print('Done')