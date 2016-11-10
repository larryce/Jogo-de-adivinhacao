Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  from random import randint
rdn= randint(0,100)
tent= 3
print("tente adivinhar o número! você tem 3 tentativas")

while tent>0:
    tent=tent-1
    num= int(input("numero:"))
    if num>rdn:
        print("o numero secreto é menor")
        print('Número de tentativas: %d' % tent)
    elif num<rdn:
        print("o numero secreto é maior")
        print('Número de tentativas = %d' % tent)
    else:
        print('Parabéns! Você acertou! O número secreto é: %d' % rdn)
        tent= -1
    if tent==0:
        print("você perdeu!")
        print('O número secreto é: %d' % rdn)
    while tent==0 or num==rdn:
        pergunta=input("você que jogar novamente sim(1) ou não(2)?")
        if pergunta==1:
            tent=3
        else:
            tent=0
            break
