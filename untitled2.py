# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:34:20 2023

@author: lcuev
"""
import numpy as np

N = 4

def deriv(ff,index,x):
    d = 0.001
    
    xp = [x[i] + d * int(i == index) for i in range(N)]
    
    return (ff(xp) - ff(x)) / d


def chriss(gs,u,v,b,x):
    return deriv(gs[u][b],v,x) + deriv(gs[v][b],u,x) - deriv(gs[u][v],b,x)


def levi_cevita(ins):
    ret = 1
    for i in ins:
        for j in ins:
            if i < j:
                ret *= (ins[j] - ins[i]) / abs(ins[j] - ins[i])
            
             
    return int(ret)       

def det(A):
    ret = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    ret += levi_cevita([i,j,k,l]) * A[0][i] * A[1][j] * A[2][k] * A[3][l]
                    
    return ret



A = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

print(det(A))
                   
            
            