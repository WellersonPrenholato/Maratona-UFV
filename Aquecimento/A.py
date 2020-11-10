N=int(input())

def mult(list):
    p = 1
    for i in list:
        p = p * i
    return p


def duploFatorial(N):
    par = N % 2 == 0 

    if ( par ):
       num =  [x for x in range(1,N+1) if x % 2 == 0 ]
    else:
       num =  [x for x in range(1,N+1) if x % 2 != 0 ]
    
    return mult(num)


print(duploFatorial(N))