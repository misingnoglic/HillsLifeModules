from random import randrange

def eightball(phenny, input):
    foo = open("8ball.txt")
    phrases = (foo.read()).split("^~`")
    phenny.say(phrases[randrange(len(phrases))])
eightball.commands = ['8']

def addresponse(phenny, input):
    foo = open("8ball.txt")
    stuff= (input.group()).split()
    phrases = str(foo.read())#.split("^~`")
    if "^~`" in str( " ".join(stuff[1:]) ):
        phenny.say("Invalid Characters")
    else:
        newphrases = phrases+"^~`"+str( " ".join(stuff[1:]) )
        foo = open("8ball.txt", 'w')
        foo.write(newphrases)
        phenny.say(str(newphrases.split("^~`")))
    
addresponse.commands = ['8add']

def removeresponse(phenny, input):
    foo = open("8ball.txt")
    stuff= ((input.group()).split())
    shat = str(" ".join(stuff[1:]))
    phrases = (foo.read()).split("^~`")
    if shat not in phrases:
        phenny.say("Not Found to delete")
    else:
        phrases.remove(shat)
        nowphrases = "^~`".join(phrases)
        foo = open("8ball.txt", 'w')
        foo.write(nowphrases)
        phenny.say(str(nowphrases.split("^~`")))
removeresponse.commands = ["8del"]

def balldefault(phenny, input):
    foo = open("8ball.txt", 'w')
    foo.write("Yes^~`No^~`Maybe^~`Ask Again Later^~`Isn't it obvious?")
    showresponses(phenny,input)
balldefault.commands = ["8default"]

def showresponses(phenny,input):
    foo = open("8ball.txt")
    phrases = (foo.read()).split("^~`")
    phenny.say(str(phrases))
showresponses.commands = ["8show"]

def ballhelp(phenny,input):
    phenny.say ("Type .8 to get your answer, .8add ANSWER to add a result, .8del ANSWER to delete an existing answer, .8show to show all possible answers, and .8default to reset the answers. Have fun!")

ballhelp.commands = ['8help'] 