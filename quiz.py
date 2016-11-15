import random as joon
from flask import Flask



class GFriend:
    SOWON = 0
    YERIN = 1
    EUNHA = 2
    YUJU = 3
    SINB = 4
    UMJI = 5    

OFFBYONE = 1.0 / 3
ALMOST = 0.5

def givePoints(key, results, i):
    results[key[i]] += 1
    
    if(i == 0):
        results[key[i+1]] += ALMOST
    elif(i == 5):
        results[key[i-1]] += ALMOST
    else:
        results[key[i-1]] += OFFBYONE
        results[key[i+1]] += OFFBYONE    
    return 1
    
def main(details = False):
    go = False
    while not go:
        a = raw_input('Which GFriend member is your soulmate? ' + \
        'Would you like to find out? \n y or n: \n')
        if(a == 'y'):
            go = True
        else:
            print "Fine then fuck you."
            
    print 'How much do you agree with the following statements,'
    print ('from 1-6 with 6 being the most \n')
    gfriend = ['Sowon', 'Yerin', 'Eunha', 'Yuju', 'SinB', 'Umji']


    results = [0.0] * 6

    i = getInput("I sing well: ") - 1
    rankingKey = [GFriend.SOWON, GFriend.UMJI, GFriend.YERIN, GFriend.SINB, GFriend.EUNHA, GFriend.YUJU]
    givePoints(rankingKey, results, i)
        

    i = getInput("I dance well: ") - 1
    rankingKey = [GFriend.SOWON, GFriend.EUNHA, GFriend.UMJI, \
                  GFriend.YUJU, GFriend.YERIN, GFriend.SINB]
    givePoints(rankingKey, results, i)

    i = getInput("I am a visual: ") - 1
    rankingKey = [GFriend.UMJI, GFriend.YUJU, GFriend.EUNHA, \
                  GFriend.SINB, GFriend.YERIN, GFriend.SOWON]
    givePoints(rankingKey, results, i)     

    i = getInput("I am a cutie pie: ") - 1
    rankingKey =  [GFriend.YUJU, GFriend.SOWON, GFriend.SINB, \
                  GFriend.YERIN, GFriend.UMJI, GFriend.EUNHA]
    givePoints(rankingKey, results, i)  
    
    i = getInput("I have a 4D personality: ") - 1
    rankingKey =  [GFriend.EUNHA, GFriend.UMJI, GFriend.SOWON, \
                    GFriend.SINB, GFriend.YUJU, GFriend.YERIN]  
    givePoints(rankingKey, results, i) 
       
    i = getInput("I am mature: ") - 1
    rankingKey =  [GFriend.YERIN, GFriend.UMJI, GFriend.SINB, \
                      GFriend.YUJU, GFriend.EUNHA, GFriend.SOWON]
    givePoints(rankingKey, results, i) 
                
        
        
    i = getInput("I am Joe's favorite <3: ") - 1
    rankingKey =  [GFriend.SOWON, GFriend.YERIN, GFriend.UMJI, \
                          GFriend.YUJU, GFriend.SINB, GFriend.EUNHA]    
    givePoints(rankingKey, results, i) 
         
    point = max(results)
    final = []
    for i in range(6):
        if(results[i] == point):
            final.append(gfriend[i])
    print "\nThe member you matched with is....... "
    print '%s!!!!!!' %joon.choice(final)
    if(details):
        print "(you could have matched with anyone here): "
        print final
        print results



def getInput(message):
    while True:
        test = raw_input(message)
        try:
            result = int(test)
            if(result > 6 or result < 1):
                raise ValueError("Pick from 1 - 6")
            return result

        except ValueError:
            print 'Pick an integer from 1 - 6 please'
    print test
    
#if __name__ == "__main__":
