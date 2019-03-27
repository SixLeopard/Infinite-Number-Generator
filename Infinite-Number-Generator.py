import random
dab = 1
while dab == 1:
    loop = 1
    f = open('Rand.txt','w')
    while loop < 500:
        lol = str(random.randint(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000))
        f.write(lol)
        loop += 1

    f = open("Rand.txt","r")
    t = open("Rand_Read.txt","w+")
    awesoness = f.read()
    t.write(awesoness)
    print(awesoness)
    f.close()

