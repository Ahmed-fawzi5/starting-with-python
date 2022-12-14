fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    new_line=line.split()
    #print(new_line[0])

    if new_line[0]!= 'from' :
        print('igone')
        continue
    else :
    print(new_line[0])
