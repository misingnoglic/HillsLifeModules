def lmgtfy(phenny, input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('http://lmddgtfy.net/?q='+phrase)

lmgtfy.commands = ['lmgtfy']

def lmgtfy_feeling_lucky(phenny,input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('http://lmddgtfy.net/?q=!%20'+phrase+'')

lmgtfy_feeling_lucky.commands = ['lmgtfylucky']
