def main():
    #escribe tu código abajo de esta línea
    print("METODO DE EULER-CAUCHY")
    print("======================")

    # Ecuacion Diferencial
    f = lambda x,y : -2 * x ** 3 + 12 * x ** 2 - 20 * x + 8.5

    # Condiciones iniciales
    x=[0]
    y=[1]

    ls=4
    h=0.5

    i=1
    while i * h <= ls:
        x = x + [(x[i-1]+h)]
        y = y + [(y[i-1] + f(x[i-1],y[i-1])*h)]

        i=i+1

    print("Tabla Método de Euler")
    print("=====================")

    print(x)
    print(y)

if __name__=='__main__':
    main()
