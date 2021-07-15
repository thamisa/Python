print("Bem vindo ao quiz!")

playing = input("Vamos jogar? ")

if playing.lower() != "sim":
    print("Okay. Até mais :(") 
    quit()

print("Okay! Vamos jogar :)")
score = 0

answer = input("O tigre é um animal: \n A)Mamífero \n B)Ovíparo \n")
if answer.lower() != "a":
    print("Incorreto! :(")
else:
    print("Correto! Vamos continuar :D\n")
    score += 1

answer = input("Qual animal representa o Brasil? \n A)Tartaruga Jonathan \n B)Vira lata amarelo \n C)Pirarucu \n")
if answer.lower() != "b":
    print("Incorreto! :(")
else:
    print("Correto! Vamos continuar :D \n")
    score += 1

answer = input("Ácido ascórbico é o nome de que vitamina? \n A)Vitamina A \n B)Vitamina B \n C)Vitamina C \n")
if answer.lower() != "c":
    print("Incorreto! :(")
else:
    print("Correto! Vamos continuar :D\n")
    score += 1

answer = input("Qual o próximo número da sequência '1, 1, 2, 3, 5, 8'? \n A)9 \n B)13 \n C)21 \n")
if answer.lower() != "b":
    print("Incorreto! :(")
else:
    print("Correto!:D\n")
    score += 1

if score == 4:
    print("Parabéns! Você acertou todas questões!")
elif score >= 1:
    print("Parabéns! Você acertou " + str((score / 4) * 100) + "% das questões!")
else:
    print("Poxa, você acertou nenhuma questão :( \nMais sorte da próxima vez.")
