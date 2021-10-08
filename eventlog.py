

# my19n077.elg - event log file from old MY Series 
# my200-10n0111.elg - event log file from new platform

file = open('C:\my19n077.elg')
# file = open('C:\my200-10n0111.elg') 

for line in file:
    line = line.strip('\n').split(';')
    print(line[0])

file.close()