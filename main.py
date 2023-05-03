g=int(input("digite o grau da equaçao:"))
if g <1 or g >2:
    print("grau invalido")
else:
    if g==1:
        print("a equaçao é do primeiro grau")
        a= float(input("digite o valo de a:"))
        if a==0:
            print("valor de a inválido.")
        else:
            b=float(input("digite o valo de b:"))
            x=-b/a
            print("o valor da raiz é: {:.2f}".format(x))
    else: 
        print("a equaçao é do segundo grau.")
        a=float(input("digite o valor de a:"))
        if a==0:
            print("valor de a inválido.")
        else:
            b=float(input("digite o valor de b:"))
            c=float(input("digite o valor de c:"))
            delta=b**2-4*a*c
            if delta < 0:
              print("nao exitem raixes reais para a equação")
            elif delta==0:
                x= -b/2*a
                print("a equaçao so tem uma raiz real: {:.2f}".format(x))
            else:
             x1 = (-b + math.sqrt(delta))/(2*a)
             x2 = (-b - math.sqrt(delta))/(2*a)
            print("A equação possui duas raízes reais: {:.2f} e {:.2f}".format(min(x1,x2), max(x1,x2)))
