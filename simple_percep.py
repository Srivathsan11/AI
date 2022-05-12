inst = [["mi",11,13],["mi",9,12],["mi",8.5,18],["mi",12,8],["mi",13,18],["a",18,5],["a",20,7.5]
     ,["a",16.5,6],["a",19,6.5],["a",12,9]]

w = [0.3,0.6]


alpha = 0.0001

wPrev = []
while(wPrev!=w):
    wPrev = w[:]        
    for i in range(len(inst)):
        x = 0
        for j in range(len(w)):
            x += inst[i][j+1]*w[j]
        print(i+1," : x ->",x)
        if x > 0 and inst[i][0] != "mi":
            for j in range(len(w)):
                w[j] = round(w[j] + alpha*(-1)*inst[i][j+1],3)
            print(w)
        if x < 0 and inst[i][0] != "a":
            for j in range(len(w)):
                w[j] = round(w[j] + alpha*(1)*inst[i][j+1],3)
            print(w)
            