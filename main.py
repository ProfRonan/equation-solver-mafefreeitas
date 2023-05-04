grau_equacao=float(input('qual o grau da equação?'))
if grau_equacao < 1 or grau_equacao > 2:
    print('Grau inválido')
elif grau_equacao==1:
    print('A equação é do primeiro grau')
    a=float(input('digite o valor de a:'))
    if a==0:
        print('Valor de a inválido.')
    else:
        b=float(input('digite o valor de b:'))
        raiz_grau1=-(b)/a
        print(f'a raiz é {raiz_grau1:,.2f}')
if grau_equacao==2:
    print('A equação é do segundo grau.')
    a=float(input('digite o valor de a:'))
    if a ==0:
        print('Valor de a inválido')
    else:
        b=float(input('digite o valor de b:'))
        c=float(input('digite o valor de c:'))
        delta=b**2-4*a*c
        if delta <0:
            print('A equação não possui raízes reais.')
        elif delta ==0:
            print('A equação possui um raíz real.')
            raiz_real=-(b)/2*a
            print(f'A equação possui apenas uma raíz real{raiz_real:,.2f}')
        else:
            print('A equação possui duas raizes reais')
            reaiz_r1=(-b-(delta**0.5))/(2*a)
            raiz_r2=(-b+(delta**0.5))/(2*a)
            if raiz_r1 < raiz_r2:
                print(f'A raiz real 1 é{raiz_r1:,.2f} e a raiz real 2 é {raiz_r2:,.2f}')
            else:
                print(f'a raiz real 1 é {raiz_r2:,.2f} e a raiz real 2 é{raiz_r1:,.2f}')
        
