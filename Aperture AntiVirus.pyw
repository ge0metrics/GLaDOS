from modules.GLaDOS import GLaDOS
import random,time

glados=GLaDOS()

activities=[glados.whee,glados.fixpc,glados.motivate,
            glados.nag]

while True:
    t=random.randint(0,500) # about 8 minutes max interval between actions
    time.sleep(t)
    random.choice(activities)()

