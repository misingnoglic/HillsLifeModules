from random import randrange

def roul(phenny, input):
    luck_array = [0,1,2,3,4,5]
    #while len(luck_array) > 0:
    if luck_array[randrange(len(luck_array))] == 0:
        phenny.say("Ooooh, gruesome, you're dead")
        phenny.write(['KICK', input.nick])
    else: del luck_array[-1]

roul.commands = ['roul']

        

