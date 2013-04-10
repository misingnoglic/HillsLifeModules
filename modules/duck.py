def duck(phenny, input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('https://duckduckgo.com/?q='+phrase)

duck.commands = ['d','duck']

    
def lmddg(phenny, input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('http://lmddgtfy.net/?q='+phrase)

lmddg.commands = ['lmddg','lmddgtfy','lmd','lm']

def duckluck(phenny, input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('https://duckduckgo.com/?q=!%20'+phrase)

duckluck.commands = ['dl','duckluck','imfeelingducky']

