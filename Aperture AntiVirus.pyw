from modules.GLaDOS import GLaDOS
import random,time

glados=GLaDOS()

activities=[glados.whee,glados.blah,
            glados.fixpc,glados.motivate,
            glados.hello,glados.deaths,
			glados.present]

while True:
    t=random.randint(0,500)
    time.sleep(t)
    random.choice(activities)()

