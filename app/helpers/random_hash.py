import random
import string

def uniqueFileName(fileName):
    random1 = random.randint(20000,32000) 
    random2 = random.randint(20000,32000) 
    random3 = random.randint(20000,32000)
    
    characters = string.ascii_letters + string.digits
    password =  "".join(random.choice(characters) for x in range(random.randint(8, 16)))
    newfile = str(random1) + str(random2) + str(random3) + password + fileName 

    return newfile