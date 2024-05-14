import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random


c = string.ascii_lowercase + string.digits
print(random.choice(c))

str = ''

for i in range(5):
    for x in random.choice(c):
        str.join(x)
print(str)

str = ''.join(random.choice(c) for x in range(5))
print(str)