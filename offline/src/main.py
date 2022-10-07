import os, time
import numpy as np
from variable_2 import var2
from variable_3 import var3

print(os.environ['var1'])
print(os.environ['var2'])

while True:
    time.sleep(2)
    var3 = var3+1
    print(f'{var3} : {np.random.randint(1,101)}')