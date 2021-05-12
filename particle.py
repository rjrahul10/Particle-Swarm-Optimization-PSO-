# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:16:38 2021

@author: Rahul Kumar
"""
import random 
from fitness import Fitness
maxiter =100
import math
class Particle:
    
    def __init__(self,x):
        global nd 
        nd = len(x);
        self.pos = []  #particle position
        self.vel = [] #particle velocity
        self.pbest =[] #particles best position
        self.val_pos =100.0 #fitness value at position
        self.val_pbest =100.0 #fitness value at best position
        for i in range(0,nd):
           self.vel.append(random.uniform(-1,1))
           self.pos.append(x[i])
            
    def analyse(self,name):
        self.val_pos = Fitness.ffc(self.pos,name)
        if self.val_pos < self.val_pbest:
            self.val_pbest = self.val_pos
            self.pbest = self.pos
            
    def vel_update(self,gbest,i):#,cbest):#,cbest):  #change parameter for ibest,ebest
        w=0.5       # constant inertia weight 
        c1=(2-0.5)*((maxiter-i)/maxiter) + 1.5     # cognative constant
        c2=(2-0.5)*((maxiter-i)/maxiter)+ 1.5      # social constant
        c3= c1*(1-math.exp(-(c1*i))) 
        r1=random.random()
        r2=random.random()
        r3=random.random()        
        for i in range(0,nd):            
            vel_cog=c1*r1*(self.pbest[i]-self.pos[i])
            vel_soc=c2*r2*(gbest[i]-self.pos[i])
            #vel_ibest=c3*(ibest[i]-self.pos[i])
            #vel_cbest = c3*r3*(cbest[i]-self.pos[i])
            self.vel[i]=w*self.vel[i]+vel_cog+vel_soc#+vel_cbest#+vel_cbest
            
    def pos_update(self,bounds):
        for i in range(0,nd):
            self.pos[i]=self.pos[i]+self.vel[i]
            #postion clamping
            self.pos[i]=min(self.pos[i],float(bounds[i][1]))
            self.pos[i]=max(self.pos[i],float(bounds[i][0]))
            