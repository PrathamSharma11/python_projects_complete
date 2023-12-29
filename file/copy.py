with open("file/sample.txt",'r') as f:
    a =f.read()

with open("file/sample2.txt",'w') as f:        #or you can write only file name instead of file and folder name
    b =f.write(a)
    print(b)



    
