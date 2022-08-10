#This simple program reads a file and prints the number of lines,
#words, and characters.
filename = input("Enter a file name: ")

try:
    fh = open(filename, 'r')
except:
    print("Error: file '" + filename + "' not found.")
    quit()

charcount = linecount = wordcount = tlc = 0
longestline = llnum = 0

for line in fh:
    tlc += 1
    if line != "":
        splitline = line.rstrip()

        if splitline != "":
            linecount += 1
            if len(splitline) > longestline:
                longestline = len(splitline)
                llnum = tlc

            splitline = splitline.split()
            wordcount += len(splitline)

            for word in splitline:
                charcount += len(word)

print("Number of lines:", linecount)
print("Number of lines, including blank lines:", tlc)
print("Number of words:", wordcount)
print("Number of characters:", charcount)
print("The longest line is", longestline, "characters long, at Line", llnum)
