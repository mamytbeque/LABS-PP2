import os
os.chdir("mian")

with open("1.py", 'r') as source:
    with open("copied.txt", 'w') as copy:
        for line in source:
            copy.write(line)
