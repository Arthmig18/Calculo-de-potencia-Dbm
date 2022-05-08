
prx = float(input('Valor da PRX em dbm da OLT: '))
conector = int(input('Quantos conector: '))
fusao = int(input('Quantas Fusões: '))
kmFibra = float(input('Quantos km de rede:'))
dbConector = conector * 0.5
dbFusao = fusao * 0.1
dbKmFibra = kmFibra * 0.25
splinter = int(input("Tem splinter:\n[1]SIM\n[2]NÃO\nRESPOSTA: \n"))
if (splinter == 1):
      tipoSplinter = int(input('Qual tipo de Splinter:\n[1]Balaceado\n[2]Desbalanceado\nRESPOSTA: \n'))
      if (tipoSplinter == 1):
            divisaoSplinter = int(input('Qual tipo de divisão:\n[1]1/2\n[2]1/4\n[3]1/8\n[4]1/16\n[5]1/32\n[6]1/64\nRESPOSTA: \n'))
            qtdSplinter = int(input('Quantos Splinter: '))
            if(divisaoSplinter == 1):
                  dbDivisao = qtdSplinter * 3.70
            elif(divisaoSplinter == 2):
                  dbDivisao = qtdSplinter * 7.30
            elif (divisaoSplinter == 3):
                  dbDivisao = qtdSplinter * 10.50
            elif (divisaoSplinter == 4):
                  dbDivisao = qtdSplinter * 13.70
            elif (divisaoSplinter == 5):
                  dbDivisao = qtdSplinter * 17.10
            elif (divisaoSplinter == 2):
                  dbDivisao = qtdSplinter * 20.50

      db = dbFusao + dbConector + dbDivisao + dbKmFibra
      dbm = prx-db
      print(dbm)
elif(splinter == 2):
      dbConector = conector * 0.5
      dbFusao = fusao * 0.1
      dbKmFibra = kmFibra * 0.25
      db = dbFusao + dbConector + dbKmFibra
      dbm = prx - db
      print(dbm)
