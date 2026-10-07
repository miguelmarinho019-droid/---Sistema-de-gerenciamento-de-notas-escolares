# Tabelas de notas  vazias

matematica = []
portugues = []
historia = []
geografia = []
biologia = []

# Função de escolha de matéria
def consultar_materia():
     print("======================================================")
     print("Qual matéria você deseja ?")
     materia = int(input("1 - Matemática. 2 - Português. 3 - História. 4 - Geografia. 5 - Biologia:  "))
     if materia == 1:
          return matematica
     elif materia == 2:
          return portugues
     elif materia == 3:
           return historia
     elif materia == 4:
          return geografia
     elif materia == 5:
          return biologia

# Função acrescentar notas
def acrescentar_nota():
    materia_escolhida = consultar_materia()
    notas = float(input("Digite uma nota (Se não tiver mais, digite 11 para sair): "))
    if notas < 11 and notas >= 0:
        materia_escolhida.append(notas)
    while notas < 11 and notas >= 0:
          notas = float(input("Digite uma nota (Se não tiver mais, digite 11 para sair): "))
          if notas < 11 and notas >= 0:
                materia_escolhida.append(notas)  




# Médias indivuais (Para o registro do relatório)
def medias_individuais(): 

 media_matematica = 0
 if len(matematica) > 0:
      total_matematica = 0
      for numero in matematica:
          total_matematica += numero
      media_matematica = total_matematica / len(matematica)

 media_portugues = 0

 if len(portugues) > 0:
      total_portugues = 0
      for numero in portugues:
          total_portugues += numero

      media_portugues = total_portugues / len(portugues)


 media_historia = 0

 if len(historia) > 0:
      total_historia = 0
      for numero in historia:
        total_historia += numero

      media_historia = total_historia / len(historia)


 media_geografia = 0

 if len(geografia) > 0:
      total_geografia = 0
      for numero in geografia:
          total_geografia += numero

      media_geografia = total_geografia / len(geografia)


 media_biologia = 0

 if len(biologia) > 0:
      total_biologia = 0
      for numero in biologia:
          total_biologia += numero

      media_biologia = total_biologia / len(biologia)

 return media_matematica, media_portugues, media_historia, media_geografia, media_biologia




# Função de cálculo de média específica
def calculo():
        total = 0
        notas = consultar_materia()
        if len(notas) > 0:
         for nota in notas:
              total += nota
         media = total / len(notas)
         return media
        else:
             print("Não tem nenhuma nota nesta matéria. ")


# Função de apresentar média de matéria específica
def apresentar_media():
      media = calculo()
      if media == None:
           print("Não tem nenhuma nota nesta matéria. ")
      else:
         print(f"Sua média é de {media}")

# Função de aprovação
def aprovaçao():
      media_matematica, media_portugues, media_historia, media_geografia, media_biologia = medias_individuais()
      if (media_biologia >= 6) and (media_geografia >= 6) and (media_historia >= 6) and (media_matematica >= 6) and (media_portugues >=  6):
            print("Situação: Aprovado ! ")
      elif (len(biologia) == 0) or (len(geografia) == 0) or (len(historia) == 0) or (len(matematica) == 0) or (len(portugues) == 0):
           print("Ainda não é possível determinar a situação ! ")
      else:
           print("Reprovado !")

# Função de Relatório
def relatorio():
      media_matematica, media_portugues, media_historia, media_geografia, media_biologia = medias_individuais()
      if len(matematica) == 0 and len(portugues) == 0 and len(historia) == 0 and len(geografia) == 0 and len(biologia) == 0:
           print("Sem notas para exibição. ")
      else:
       print("Suas notas são:")


       if len(matematica) == 0:
        print("Sem notas em matemática ! ")
       else:
        print(f"Em matemática: {matematica} > média > {media_matematica} ")


       if len(portugues) == 0:
           print("Sem notas em português ! ")
       else:
           print(f"Em português: {portugues} média >  {media_portugues} ")

       if len(historia) == 0:
           print("Sem notas em história ! ")
       else:
          print(f"Em história: {historia} média > {media_historia} ")

       if len(geografia) == 0:
           print("Sem notas em geografia ! ")
       else:
          print(f"Em geografia: {geografia} média > {media_geografia} ")

       if len(biologia) == 0:
           print("Sem notas em biologia !")
       else:  
          print(f"Em biologia {biologia} média > {media_biologia} ")


# Função do menu
def menu():
 mais_opçoes = 1
 while mais_opçoes == 1:
           opçoes = int(input("O que deseja ? (1- Adicionar notas em matérias. 2 - Consultar média. 3 - Consultar relatório. 4 - Situação atual de provação/reprovação): "))

           if opçoes == 1:
            acrescentar_nota()

           if opçoes == 2:
            apresentar_media()
            print("Obrigado por usar nossos serviços !")

           if opçoes == 3:
            relatorio()
            aprovaçao() 

           if opçoes == 4:
            aprovaçao()

           mais_opçoes = int(input("Deseja algo a mais ?( 1 - Sim. 2 - Não. ): "))
 else:
          print("Agrademos por usar o nosso sistema !")







# Entrada de informações
nome = str(input("Olá aluno, digite seu nome: "))
menu()





