def add(a:int,b:int)->int:
    return a+b

def fakultaet(n:int)->int:
    return 1 if n<=1 else n*fakultaet(n-1)

if __name__=='__main__':
    print('Add(2,5)=', add(2,5))
    print('Fakultät(5)=', fakultaet(5))
