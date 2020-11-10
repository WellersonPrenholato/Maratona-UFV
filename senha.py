inp = input()
[A,B] = [int(x) for x in inp.split(' ')]

s = [A,B, A+B, A-B, B-A]
for i in range(1,101):
    
    if ( i not in s):
        print(i)
        break
