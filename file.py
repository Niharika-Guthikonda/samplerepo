fname=input('Enter file name:')
try:
     f=open(fname)
except:
    print('File can\'t be displayed')
    quit()
for line in f:
    if 'quote' not in line:
        continue
    print(line.strip())
    
