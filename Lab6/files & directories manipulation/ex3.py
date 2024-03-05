import os
path = input() #os.getswd()
if not os.path.exists(path):
        print("Path does not exist.")
        
else:
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print("Directory:", dirname)
        print("Filename:", filename)
