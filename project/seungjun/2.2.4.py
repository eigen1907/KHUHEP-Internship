b = 0

while True :
    a = int(input(''))
    if a >= 0:
        b += a 
        print(b)
    else :
        print('음수 : 중단')
        break