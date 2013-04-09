def showpoints(phenny, input):
    foo = eval((open('points.txt')).read())
    name=(' '.join(((input.group()).split())[1:])).lower()
    if name in foo.keys(): phenny.say(name + ': '+str(foo[name]))
    else:
        foo[name] = 0
        new = open('points.txt', 'w')
        new.write(str(foo))
        phenny.say("User was previously not in database, now added with 0 points")

showpoints.commands = ["showpoints", "showscore", 'score']

def addpoints(phenny, input):
    foo = eval((open('points.txt')).read())
    name=(' '.join(((input.group()).split())[1:])).lower()
    if name in foo.keys():
        foo[name]+=1
        phenny.say(name+": "+str(foo[name]))
        new = open('points.txt', 'w')
        new.write(str(foo))
    else:
        foo[name] = 1
        new = open('points.txt', 'w')
        new.write(str(foo))
        phenny.say(name+": "+str(foo[name]))
addpoints.commands = ['addpoint', 'addpoints', 'pluspoint']

def subpoint(phenny, input):
    foo = eval((open('points.txt')).read())
    name=(' '.join(((input.group()).split())[1:])).lower()
    if name in foo.keys():
        foo[name]-=1
        phenny.say(name+": "+str(foo[name]))
        new = open('points.txt', 'w')
        new.write(str(foo))
    else:
        foo[name] = -1
        new = open('points.txt', 'w')
        new.write(str(foo))
        phenny.say(name+": "+str(foo[name]))
subpoint.commands = ['subpoint', 'delpoint', 'subpoints', 'delpoints']


def winner(phenny, input):
    winners=[]
    foo = eval((open('points.txt')).read())
    if len(foo)==0: phenny.say("Nobody entered the contest yet!")
    else:
        high = max(foo.values())
        for x in foo.keys():
            if foo[x]==high: winners +=[x]
        phenny.say(', '.join(winners)+ " with "+str(foo[winners[0]])+" points")

winner.commands = ["winners",'winner']

def scores(phenny, input):
    scores = ''
    foo = eval((open('points.txt')).read())
    if len(foo)==0: phenny.say("Nobody entered the contest yet!")
    else:
        while len(foo)>0:
            high = max(foo.values())
            for x in foo.keys():
                if foo[x]==high:
                    scores += (x+": "+str(foo[x])+' ')
                    del foo[x]        
        for string in breakupstring(scores):
            phenny.say(string)

        


scores.commands = ['scores','leaders','showscores']

def scoresraw(phenny, input):
    foo = eval((open('points.txt')).read())
    phenny.say(str(foo))

scoresraw.commands = ['scoresraw']
def resetscore(phenny, input):
    foo = eval((open('points.txt')).read())
    name=(' '.join(((input.group()).split())[1:])).lower()
    if name in foo:
        del foo[name]
        new = open('points.txt', 'w')
        new.write(str(foo))
        phenny.say('score reset for user')

resetscore.commands = ['resetscore','resetpoints']

def breakupstring(string):
    LOS = []
    while len(string)>437:
        newstr = string[:437]
        LOS+=[newstr]
        string = string[437:]
    LOS += [string]
    return LOS

def pointshelp(phenny, input):
    phenny.say('''Welcome to points, where the points don't matter! Type .showpoints USER to see their points, .addpoint USER to give them a point, .subpoint USER to make them lose a point, .resetscore USER to reset someone's score, .winners to see who is in the lead, and .scores to see all the scores. Have fun!''' )

pointshelp.commands = ['pointshelp','phelp']
