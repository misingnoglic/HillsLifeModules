def duck(phenny, input):
    phrase = input.group(2)
    phrase = phrase.split()
    phrase = '%20'.join(phrase)
    phenny.say('https://duckduckgo.com/?q='+phrase)

lmgtfy.commands = ['d']

    
