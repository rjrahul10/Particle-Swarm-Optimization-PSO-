# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:14:02 2021

@author: Rahul Kumar
"""
import random
import csv
import pandas as pd
from particle import Particle
itr_max =100
np = 10

data = pd.read_csv('weierstrassresult.csv')
                
class PSO:
    def __init__(self, x, bounds, np, name):
        global nd;
        gbest = [] #global best for the swarms
        all_gbest =[] # list to store all the gbest
        i_all = []
        val_gbest = 100
        val_cbest = 100
        cbest =[]
        swarm =[] #creating the swarms
        for i in  range(np):
            swarm.append(Particle(x))
        
        #PSO iteration starts
        
        i = 0
        while i<itr_max:
            for j in range(np):
                swarm[j].analyse(name)
                
                #finding gbest
                if abs(swarm[j].val_pbest-0.0) < abs(0.0-val_gbest):
                    val_gbest = swarm[j].val_pbest
                    gbest = swarm[j].pbest
                if abs(0.0-swarm[j].val_pos) < abs(0.0-val_cbest):
                    val_cbest = swarm[j].val_pos
                    cbest = swarm[j].pos
            #with open('sphereresult.csv','w') as file:
             #   a = csv.writer(file)
              #  a.writerow({'Iteration':i+1})
              #  a.writerow({'Std PSO': val_gbest})
            #file.close()
            i_all.append(i+1)
            all_gbest.append(val_gbest)
            r3=random.randint(0,np-1)
            ibest=swarm[r3].pos
            for j in range(0,np):
                swarm[j].vel_update(gbest,i,cbest)#,cbest)#,cbest)
                swarm[j].pos_update(bounds)
            i+=1
       # data['Iteration'] = i_all
        data['Cbest'] = all_gbest
        #data['Cbest'] = all_gbest
        #data.to_csv('weierstrassresult.csv')
        print("\n\nResults\n")
        print("The best postion for funtction is ", gbest)
        print("The value is ", val_gbest)
        

if __name__ == "__main__":
    
    #for sphere function
    initial=[0.5,0.5]#,0.5,0.5,0,0.5,0.5,0.5,0,0.5]               # initial starting location [x1,x2...]
    bounds=[[-0.5,0.5],[-0.5,0.5]]#,[-0.5,0.5],[-0.5,0.5],[-0.5,0.5],[-0.5,0.5],[-0.5,0.5],[-0.5,0.5],[-0.5,0.5],[-0.5,0.5]]#[-10,10],[-10,10],[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
    PSO(initial,bounds,np,"weierstrass")
