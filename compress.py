# compress.py
# Devise an effective and efficient lossless compression algorithm
# for compressing large textual documents.
# @, # , &, *

try:
    infile = open('flintstones.txt','r')
    outfile = open('cflintstones.txt','w')
    char = 0
    consec = 1
    
    for line in infile:
        while char+1 != len(line):
            if line[char] == line[char+1]:
                consec += 1
                char += 1
            else:
                if consec == 1:
                    outfile.write(line[char])
                    char +=1
                else:
                    outfile.write(line[char]+str(consec))
                    char += 1
                    consec = 1
        char = 0
        outfile.write(line[char]+str(consec)+'\n')



            
##        words = line.split()
##        for word in words:


    infile.close()
    outfile.close()

except IOError:
    print("Error in reading fintstones.txt.")
