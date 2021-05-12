# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:16:24 2021

@author: Rahul Kumar
"""
import math
import random
class Fitness:
    def sphere(x):
        sum =0
        for i in range(len(x)):
            sum += x[i]**2
        return sum
    def quartic(x):
        sum = 0
        for i in range(len(x)):
            sum += (i + 1) * pow(x[i], 4) + random.gauss(0, 1)
        return sum
    def grienwank(x):
        sum = 0
        mul = 1
        for i in range(1, len(x) + 1):
            sum += pow(x[i - 1], 2)
            mul *= math.cos(x[i - 1] / math.sqrt(i))
        return sum / 4000 - mul + 1
    def rastrigin(x):
        sum = 0
        for xi in x:
            sum += xi * xi - 10 * math.cos(2 * math.pi * xi) + 10
        return sum
    def ackley(x):
        sum_a = 0
        sum_b = 0
        n = len(x)
        for xi in x:
            sum_a += pow(xi, 2)
            sum_b += math.cos(2 * (math.pi) * xi)
        return 20 + math.e - 20 * math.pow(math.e, math.sqrt(sum_a / n) - math.pow(math.e, sum_b / n))
    def alpine(x):
        sum = 0.0
        n = len(x)
        for xi in x:
            sum += abs(xi * math.sin(xi) + 0.1 * xi)
        return sum 
    def step(x):
        sum = 0.0
        for xi in x:
            sum += ((xi+0.5)*(xi+0.5))
        return sum
    def weierstrass(x):
        sum =0.0
        for xi in x:
            for k in range(20):
                sum += (math.pow(0.5,k)*math.cos((2*math.pi)*pow(3,k)*(xi+0.5)))
        return sum
    def ffc(x,name):
        if name == "sphere":
            sum=Fitness.sphere(x)
        elif name == "quartic":
            sum = Fitness.quartic(x)
        elif name == "grienwank":
            sum = Fitness.grienwank(x)
        elif name == "rastrigin":
            sum = Fitness.rastrigin(x)
        elif name == "ackley":
            sum = Fitness.ackley(x)
        elif name == "alpine":
            sum = Fitness.alpine(x)
        elif name == "step":
            sum = Fitness.step(x)
        elif name == "weierstrass":
            sum = Fitness.weierstrass(x)
        return sum