import os
import random

os.mkdir("example")
print(123)
for i in range(100):
    with open("./example/" + str(i) + ".txt", "wb") as file:
        file.write(random.randbytes(random.randint(1024, 102400)))
