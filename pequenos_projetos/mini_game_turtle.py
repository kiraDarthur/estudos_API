from turtle import Turtle

#iniciar  uma turtle
t = Turtle()
#definir a velocidade
t.speed(1)
while True:
    direcao =input("Para qual direção devemos ir? f:frente ou t trás")
    if direcao =='f':
        distancia = int(input("Qual pixels devemos movimentar para a frente "))
        movimentar_para_lado = input('Rotacionar para d:direita , e:esquerda n:nao rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input("Quanto para a direita devemos rotacionar ?"))
            t.right(angulo)
        elif movimentar_para_lado == "e":
            angulo = int(input("Quanto para esquerda devemos rotaciona?"))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(input("Qual pixels devemos movimentar para a frente "))
        movimentar_para_lado = input('Rotacionar para d:direita , e:esquerda n:nao rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input("Quanto para a direita devemos rotacionar ?"))
            t.right(angulo)
        elif movimentar_para_lado == "e":
            angulo = int(input("Quanto para esquerda devemos rotaciona?"))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continuar andando ?')
    if resposta not in ('sim','s'):
        break


