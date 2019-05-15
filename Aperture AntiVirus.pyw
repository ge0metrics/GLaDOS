from modules.GLaDOS import GLaDOS
import random,time

glados=GLaDOS()

activities=[glados.whee,glados.blah,
            glados.fixpc,glados.motivate]

while True:
    t=random.randint(0,100)
    time.sleep(t)
    random.choice(activities)()

