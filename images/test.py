# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:38:40 2022

@author: jadej
"""

inp=int('01001000',2)

def flip(num,x):
    if(x>128):
        return num
    
    if(num&x==0):        
        return num+x
    else:
        return num-x
    

def distance(inp):
    f=0
    l=0
    c=1
    pos=[]
    sinp=inp
    print("{0:b}".format(inp))
    print(inp)
    while(sinp):        
        dig=sinp&1
        if(dig==1):
            if(f==0):
                f=c
            l=c
        c*=2
        sinp>>=1
    print(inp)
    a=[1,0,-1]
    for i in a:
        s=flip(inp,int(pow(2,i)*l))
        print("flipping",l,"with ",int(pow(2,i)*l),"result is ",s)
        
        if(s!=inp):
           pos.append(s)
        s=flip(inp,int(pow(2,i)*f))
        print("flipping",f,"with ",int(pow(2,i)*f),"result is ",s)
        if(s!=inp):
           pos.append(s)
        
    print("init = {0:b}".format(inp))
    for i in pos:
        print(i," : {0:b}".format(i))
    
    return pos #"{0:b}".format(37)

distance(inp)

