
p = ['capivara', 'capivaro','capivarista', 'capivaristo']

def resp(lines):
    
    for line in lines:
        for palavra in p:
                if ( line.find(palavra) >= 0 ):
                    return 'YES'
    
    return 'NO'
lines = []

while True:
    try:
        line = input()
        line = line.lower()
        lines.append(line)
    except:
        break


print(resp(lines))