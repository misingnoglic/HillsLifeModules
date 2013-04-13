def returnresponse(phenny,input):
    foo = eval((open('responses.txt')).read())
    key = str(input.group(2))
    try:
        phenny.say(str(foo[key]))
    except:
        phenny.say("Item not found")

returnresponse.commands = ['r','respond']

def addresponse(phenny,input):
    foo = eval((open('responses.txt')).read())
    inp = str(input.group(2)).split()
    if inp[0] in foo.keys():
        phenny.say("Keyword already being used!")
    else:
        foo[inp[0]]= str(inp[1])
        new = open('responses.txt', 'w')
        new.write(str(foo))
        phenny.say("Response Added!")

addresponse.commands = ['addr','addresponse', 'radd']

def responsehelp(phenny,input):
    phenny.say("To get a response type .r CODE. To add one type .radd CODE RESPONSE. I intended this to save links but you can use it for anything")
    
responsehelp.commands = ['rhelp']
