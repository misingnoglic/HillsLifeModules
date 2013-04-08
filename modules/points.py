def showpoints(phenny, input):
    foo = eval((open('points.txt')).read())
    name=((input.group()).split())[1]
    if name in foo.keys(): phenny.say(name + ': '+str(foo[name]))
    else:
        foo[name] = 0
        new = open('points.txt', 'w')
        new.write(str(foo))

showpoints.commands = ["showpoints"]

def addpoints(phenny, input):
    foo = eval((open('points.txt')).read())
    name=((input.group()).split())[1]
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
addpoints.commands = ['addpoint']

def subpoint(phenny, input):
    foo = eval((open('points.txt')).read())
    name=((input.group()).split())[1]
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
subpoint.commands = ['subpoint']


def winner(phenny, input):
    winners=[]
    foo = eval((open('points.txt')).read())
    if len(foo)==0: phenny.say("Nobody entered the contest yet!")
    else:
        high = max(foo.values())
        for x in foo.keys():
            if foo[x]==high: winners +=[x]
        phenny.say(', '.join(winners)+ " with "+str(foo[winners[0]])+" points")

winner.commands = ["winners"]