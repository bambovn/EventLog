


file = open('log_files\old.elg')

for line in file:
    line = line.strip('\n').split(';')
    print(line[0])

file.close()