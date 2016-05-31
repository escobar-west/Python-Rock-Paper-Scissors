from __future__ import division
from math import sqrt
import random as rnd

def checkGame(a, b):
    if a == '0' and b == '1' or a == '1' and b == '2' or a == '2' and b == '0':
        return -1
    elif a == b:
        return 0
    else:
        return 1

RPS_count = { '000' : 3, '001' : 3, '002' : 3, '010' : 3, '011' : 3, '012' : 3, '020' : 3, '021' : 3, '022' : 3, '100' : 3, '101' : 3, '102' : 3, '110' : 3, '111' : 3, '112' : 3, '120' : 3, '121' : 3, '122' : 3, '200' : 3, '201' : 3, '202' : 3, '210' : 3, '211' : 3, '212' : 3, '220' : 3, '221' : 3, '222' : 3 }

RPS_disp  = {'0' : 'rock', '1' : 'paper', '2' : 'scissor'}


wins, ties, losses = 0,0,0
last2 = '33'
#T-1, T

#Loops until user presses q
while(1):
    roll = raw_input('Please type r,p,s, or q\n')
    
    while(roll not in ['r', 'p', 's', 'q']):
        roll = raw_input("Look: you've got to type r,p,s, or q\n")

    if roll == 'r':
        x = '0'
    elif roll == 'p':
        x = '1'
    elif roll == 's':
        x = '2'
    elif roll == 'q':
        quit()

    if(last2[0] == '3'):
        y = str( rnd.randint(0,2) )
    else:
        r_count = RPS_count[last2 + '0']
        p_count = RPS_count[last2 + '1']
        s_count = RPS_count[last2 + '2']

        tot_count = r_count + p_count + s_count

        q_dist = [ r_count/tot_count, p_count/tot_count, 1- (r_count/tot_count) - (p_count/tot_count) ]
        
        result = [ max(q_dist[2]-q_dist[1],0), max(q_dist[0]-q_dist[2],0), max(q_dist[1]-q_dist[0],0) ]
        resultnorm = sqrt(result[0]*result[0] + result[1]*result[1] + result[2]*result[2])
        result = [result[0]/resultnorm, result[1]/resultnorm, 1 - result[0]/resultnorm - result[1]/resultnorm]

        y = rnd.uniform(0,1)

        if y <= result[0]:
            y = '0'
        elif y <= result[0] + result[1]:
            y = '1'
        else:
            y = '2'

        #update dictionary
        RPS_count[last2+x] += 1

    last2 = last2[1] + x

    print 'You played: ' + RPS_disp[x] + '\nI played:   ' + RPS_disp[y] + '\nGAME RESULT (-1 is a loss for you):', checkGame(x,y)

    if checkGame(x,y) == -1:
        losses += 1
    elif checkGame(x,y) == 0:
        ties   += 1
    elif checkGame(x,y) == 1:
        wins   += 1

    print 'Wins:', wins, 'Losses:', losses, 'Ties:', ties