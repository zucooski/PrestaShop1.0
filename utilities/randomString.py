import string
import random

def randomStringGenerator(size=5,char=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for x in range(size))