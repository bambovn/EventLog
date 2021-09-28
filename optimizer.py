
file = open("log_files\old.elg")
file_optimized = open('log_files\optimized.elg', "w")


for line in file:
    
    if line[0] == 'M':
        continue
    else:
        file_optimized.write(str(line))




file.close()
file_optimized.close()