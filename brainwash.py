import os
import time
from graph import Graph
from printer import money as The_Economy

cycle = 0
a = "#"
stonk = 0
stonks = 10

#loading screen
for i in range(4):
    time.sleep(1)
    os.system("clear")
    print("Stonks.exe\nLoading "+(a*i))
#load stonks
for i in range(stonks):
    for o in range(5):
        time.sleep(.1)
        os.system("clear")	
        print(Graph.frame[i])
        print("Loading Stonks:\n")
        print("Stonk("+str(i+1)+") "+(a*o*8))
        print("\n\nStonks loaded: "+str(i+1+cycle)+"                   Cash: $"+str(i*742345))
        
        #display aquired stonks
        for p in range(stonk):
            print("Stonk("+str(p+1+cycle)+") #######################################")
    stonk += 1

os.system("clear")
print(Graph.stonks)
print("                                  S  T  O  N  K  S")
