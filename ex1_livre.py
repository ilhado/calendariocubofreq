# -*- coding: utf-8 -*-
"""Ex1-Livre.ipynb

"""

import matplotlib.pyplot as plt

def contaDia(day,diceZero, diceUm):
        if day == 1 :
            diceZero[1][1] += 1
            diceUm[0][1] += 1
            return
        if day == 2 :
            diceZero[2][1] +=1
            diceUm[0][1] += 1
            return
        if day == 3 :
            diceZero[3][1] +=1
            diceUm[0][1] += 1
            return
        if day == 4 :
            diceZero[4][1] +=1
            diceUm[0][1] +=1
            return
        if day == 5 :
            diceZero[5][1] +=1
            diceUm[0][1] +=1
            return
        if day == 6 :
            diceZero[0][1] +=1
            diceUm[3][1] +=1
            return
        if day == 7 :
            diceZero[0][1] +=1
            diceUm[4][1] +=1
            return
        if day == 8 :
            diceZero[0][1] +=1
            diceUm[5][1] +=1
            return
        if day == 9 :
            diceZero[0][1] +=1
            diceUm[3][1] +=1
            return
        if day == 10 :
            diceZero[0][1] +=1
            diceUm[1][1] +=1
            return
        if day == 11 :
            diceZero[1][1] +=1
            diceUm[1][1] +=1
            return
        if day == 12 :
            diceZero[2][1] +=1
            diceUm[1][1] +=1
            return
        if day == 13 :
            diceZero[3][1] +=1
            diceUm[1][1] +=1
            return
        if day == 14 :
            diceZero[4][1] +=1
            diceUm[1][1] +=1
            return
        if day == 15 :
            diceZero[5][1] +=1
            diceUm[1][1] +=1
            return
        if day == 16 :
            diceZero[1][1] +=1
            diceUm[3][1] +=1
            return
        if day == 17 :
            diceZero[1][1] +=1
            diceUm[4][1] +=1
            return
        if day == 18 :
            diceZero[1][1] +=1
            diceUm[5][1] +=1
            return
        if day == 19 :
            diceZero[1][1] +=1
            diceUm[3][1] +=1
            return
        if day == 20 :
            diceZero[0][1] +=1
            diceUm[2][1] +=1
            return
        if day == 21 :
            diceZero[1][1] +=1
            diceUm[2][1] +=1
            return
        if day == 22 :
            diceZero[2][1] +=1
            diceUm[2][1] +=1
            return
        if day == 23 :
            diceZero[3][1] +=1
            diceUm[2][1] +=1
            return
        if day == 24 :
            diceZero[4][1] +=1
            diceUm[2][1] +=1
            return
        if day == 25 :
            diceZero[5][1] +=1
            diceUm[2][1] +=1
            return
        if day == 26 :
            diceZero[2][1] +=1
            diceUm[3][1] +=1
            return
        if day == 27 :
            diceZero[2][1] +=1
            diceUm[4][1] +=1
            return
        if day == 28 :
            diceZero[2][1] +=1
            diceUm[5][1] +=1
            return
        if day == 29 :
            diceZero[2][1] +=1
            diceUm[3][1] +=1
            return
        if day == 30 :
            diceZero[3][1] +=1
            diceUm[0][1] +=1
            return
        if day == 31 :
            diceZero[3][1] +=1
            diceUm[1][1] +=1
            return

def month31(diceZero, diceUm):
  month31days = ['Jan', 'Mar', 'Mai', 'Jul', 'Ago', 'Out', 'Dez']
  for i in month31days :
      for day in range (1,32) :
        contaDia(day,diceZero, diceUm)
      

def month30(diceZero, diceUm):
  month30days = ['Abr', 'Jun', 'Set', 'Nov']
  for i in month30days :
      for day in range (1,31) :
        contaDia(day,diceZero, diceUm)
      

def month28(diceZero, diceUm) :
  month28days = ['Fev']
  for i in month28days :
      for day in range (1,29) :
        contaDia(day,diceZero, diceUm)
      
 

def main():
  diceZero = [['0 D1', 0], ['1 D1', 0], ['2 D1', 0], ['3', 0], ['4',0], ['5', 0]]
  diceUm = [['0 D2', 0], ['1 D2', 0], ['2 D2', 0], ['6ou9', 0], ['7', 0], ['8', 0]]

  month31(diceZero, diceUm)
  month30(diceZero, diceUm)
  month28(diceZero, diceUm)
  
  faces0 =  [diceZero[j][0] for j in range(len(diceZero))]  
  faces1 =  [diceUm[j][0] for j in range(len(diceUm))]
  faces = faces0 + faces1
  
  acum0 =  [diceZero[j][1] for j in range(len(diceZero))]  
  acum1 =  [diceUm[j][1] for j in range(len(diceUm))]
  acumulado = acum0 + acum1
              
  plt.plot(faces, acumulado, marker='o', linestyle='-', color='b')
  plt.title("Frequência de cada face no Calendário de 2 cubos")
  plt.xlabel("Faces")
  plt.ylabel("Ocorrências")
  plt.show()

  print("Quantidade total :")

  for k in range (0,6):
     print(diceZero[k])
  for k in range (0,6):
     print(diceUm[k])


if __name__ == "__main__":
    main()