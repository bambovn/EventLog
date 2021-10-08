#file = open('C:\my19n077.elg')
file = open('C:\my200-10n0111.elg')



# TODO: filter the appending of the tools_on before appendig in tools 
# TODO: sort the naming of the current tools and tools_on 



def current_tools():
    tc = False
    tools = []
    tools_on = []
    current_hydra_tools = []
    current_midas_tools = []

    for line in file:
        line = line.strip('\n').split(';')  


        if line[0] == 'TC2':
            #print(line)

            tools_on.append(line)
            tc = True
            continue
        elif line[0] == '-' and tc == True:
            #print(line)
            tools_on.append(line)
        elif line[0] != 'TC2' and line[0] != '-':
            tc = False
            tools = tools_on
            tools_on = []
            print(tools)




current_tools()

file.close()