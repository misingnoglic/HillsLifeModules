from random import randrange

def breakupstring(string):
    LOS = []
    while len(string)>437:
        newstr = string[:437]
        LOS+=[newstr]
        string = string[437:]
    LOS += [string]
    return LOS

#sortchoices.commands = ['8sort']
def eightball(phenny, input):
    foo = open("8ball.txt")
    phrases = (foo.read()).split("^~`")
    phenny.say(phrases[randrange(len(phrases))])
eightball.commands = ['8', '!8', '8ball']

def eightyesno(phenny,input):
    phenny.say(['Yes','No'][randrange(2)])

eightyesno.commands = ['8y','8yn']

def addresponse(phenny, input):
    #This comment doesn't do anything but adding it makes my program work

    foo = open("8ball.txt")
    stuff= (input.group()).split()
    phrases = str(foo.read())#.split("^~`")
    if "^~`" in str( " ".join(stuff[1:]) ):
        phenny.say("Invalid Characters")
    else:
        nowphrases = phrases+"^~`"+str( " ".join(stuff[1:]) )
        foo = open("8ball.txt", 'w')
        foo.write(nowphrases)
        #phenny.say(str(newphrases.split("^~`")))
        for part in breakupstring(str(nowphrases.split("^~`"))):
            phenny.say(str(part))

    
addresponse.commands = ['8add', '8balladd']

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
        for part in breakupstring(str(nowphrases.split("^~`"))):
            phenny.say(str(part))
        #phenny.say(str(nowphrases.split("^~`")))
removeresponse.commands = ["8del"]

def removeindex(phenny,input):
    foo = open("8ball.txt")
    stuff= ((input.group()).split())
    try:
        index = int(stuff[1])
        cont=True
    except:
        phenny.say("Not an integer")
        cont=False
    phrases = (foo.read()).split("^~`")
    if cont==True:
        if len(phrases)<(index-1): phenny.say("Index doesn't exist")
        else:
            del phrases[index] 
            nowphrases = "^~`".join(phrases)
            foo = open("8ball.txt", 'w')
            foo.write(nowphrases)
            for part in breakupstring(str(nowphrases.split("^~`"))):
                phenny.say(str(part))
                #phenny.say(str(nowphrases.split("^~`")))
removeindex.commands = ["8delindex"]
    

def balldefault(phenny, input):
    if input.admin==False:
        phenny.say("You need to be an admin to run this command")
    else:
        foo = open("8ball.txt", 'w')
        foo.write("Yes^~`No^~`Maybe^~`Ask Again Later^~`Isn't it obvious?")
        showresponses(phenny,input)
balldefault.commands = ["8default"]

def showresponses(phenny,input):
    foo = open("8ball.txt")
    phrases = str((foo.read()).split("^~`"))
    for part in breakupstring(phrases):
        phenny.say(part)
    
showresponses.commands = ["8show"]

def ballhelp(phenny,input):
    phenny.say ("Type .8 to get your answer, .8add ANSWER to add a result, .8del ANSWER to delete an existing answer, .8delindex INTEGER to remove that indexed answer (start counting at 0), .8show to show all possible answers, and .8default to reset the answers (trusted users only). Have fun!")

ballhelp.commands = ['8help'] 

def ballsort(phenny,input):
    foo = open("8ball.txt")
    phrases = (foo.read()).split("^~`")
    phrases.sort()
    nowphrases = "^~`".join(phrases)
    foo = open("8ball.txt", 'w')
    foo.write(nowphrases)
    for part in breakupstring(str(nowphrases.split("^~`"))):
        phenny.say(str(part))

ballsort.commands = ['8sort']

def randnumb(phenny,input):
    inp = str(input.group(2))
    a = inp.split()
    if len(a)<2: phenny.say("Invalid input, please type .rnum LOWERINT HIGHERINT - for example .rnum 1 5 will return a number from 1 to 5 (inclusive)")
    else:
        #a = [int(x) for x in a]
        phenny.say(str(randrange(int(a[0]),int(a[1])+1)))

randnumb.commands = ['rnumb','randnumb','rnum','randnub']
