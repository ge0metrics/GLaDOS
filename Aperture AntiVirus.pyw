from modules.GLaDOS import GLaDOS
import random,webbrowser

glados=GLaDOS()

activities=[glados.whee,glados.blah,
            glados.fixpc,glados.motivate]

while True:
    time.sleep(random.randint(0,1000))
    random.choice(activities)()

