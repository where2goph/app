import os
li = []
i = 1

for filename in os.listdir(os.getcwd()):
    if '.py' not in filename:
        os.rename(filename,'{}.jpg'.format(str(i)))
        i+=1
