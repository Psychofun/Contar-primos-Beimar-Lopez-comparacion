def valorB(a):
    return round(((2*a)+ ((-1)**a)-7 )/6)

def formula(x,y):
    return ((1-(2*x) -(2*y))* ((-1)**x) -((-1)**y) + (1 + (2*x))* ((-1)**(x+y)) + (12*x*x) + (6*y) + (12*x*y) - 5)/4


def limiteX(b):
    return int((((-1 + (1+3*b)**0.5))/3))

def cantidad(a,suma):
    return round(((2*a) + ((-1)**a) - (6*suma)+ 5))/6

def contarPrimos(a):
    vector = dict()

    b = valorB(a)

    limite =int(limiteX(b))
    con = 0  
    x = 1 

    while(x<= limite):
        y = 1 
        while True:
            w = formula(x,y)
            if w>b:
                break

            vector[con]= w
            con =con + 1
            y = y + 1
        x = x + 1
    
    temp = {val: key for key,val in vector.items()}
    res = {val:key  for key,val in temp.items()}

    return res 

def pi_beimar2(x):
    vector = contarPrimos(x)
    suma = len(vector)
    pi_x = int(cantidad(x,suma))

    return pi_x 

if __name__ =="__main__":
    a = 1000000

    print('Números primos menores a:', a)
    vector = contarPrimos(a)

    suma = len(vector)

    pi = cantidad(a,suma)
    print("Mediante la función W(x,y) de Beimar Wilfredo López Subia: ",pi)
    print("Cantidad de números primos: ", int(pi))