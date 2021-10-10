file = open('C:\my19n077.elg')
#file = open('C:\my200-10n0111.elg')

output_file = open('C:\output.txt', 'w')


machine_type = ''


def machineType():
    dx_machine_type = ['H1L', 'H2L', 'H2L', 'H4L', 'H5L', 'H6L', 'H7L', 'H8L',
                       'H1R', 'H2R', 'H3R', 'H4R', 'H5R', 'h5R', 'H7R', 'H8R']

    for line in file:
        line = line.strip('\n').split(';')

        if line[0] != 'M2':
            continue
        else:
            if line[-1] in dx_machine_type:
                machine_type = 'DX'
            else:

                machine_type = 'SX'
            break
    print(machine_type)


def current_tools():
    tc = False  # Flag that handles the case when we have multiple tool change lines, this in Hydra tool chane cases
    total_tools_change_time = 0  # The time is in miliseconds
    tools = ''
    tools_on = ''

    items = []  # Holder before adding line in file
    skip = ['A right Front',
            'A right Back',
            'B right Front',
            'B right Back',
            'C right Front',
            'C right Back',
            'A left Front',
            'A left Back',
            'B left Front',
            'B left Back',
            'C left Front',
            'C left Back',
            'A Front',
            'B Back',
            'A Back',
            'B Front',
            'C Front',
            'C Back',
            '', '-', 'TC2']

    # SX
    current_midas_tool = ''
    current_hydra_tools = {
        "H1": '', "H2": '', "H3": '', "H4": '', "H5": '', "H6": '', "H7": '', "H8": ''
    }
    current_midas_tools = ''

    # DX
    current_hydra_tools_R = {
        "H1": '', "H2": '', "H3": '', "H4": '', "H5": '', "H6": '', "H7": '', "H8": ''
    }
    current_hydra_tools_L = {
        "H1": '', "H2": '', "H3": '', "H4": '', "H5": '', "H6": '', "H7": '', "H8": ''
    }
    current_midas_tool_R = ''
    current_midas_tool_L = ''

    for line in file:
        line = line.strip('\n').split(';')

        if line[0] == 'TC2':
            total_tools_change_time += int(line[1])
            tools_on += line
            tc = True
            continue
        elif line[0] == '-' and tc == True:
            tools_on += line
        elif line[0] != 'TC2' and line[0] != '-':
            tc = False
            tools = tools_on
            tools_on = []
            if len(tools) == 0:
                continue
            else:
                # print(tools)
                for item in tools:
                    if item in skip or item.isnumeric():
                        continue
                    else:
                        items.append(item)

                # Example for DX
                # Midas
                # ['ZR', 'A12', 'A12']
                # ['ZL', 'NOTOOL', 'C14']
                # Hydra
                #['H1R', 'H02', 'H2R', 'H02', 'H3R', 'H02', 'H4R', 'H02', 'H5R', 'H02', 'H6R', 'H02', 'H7R', 'H02', 'H8R', 'H02']
                #['H1L', 'H01', 'H2L', 'H01', 'H3L', 'H02', 'H4L', 'H01', 'H5L', 'H01', 'H6L', 'H01', 'H7L', 'H01', 'H8L', 'H01']

                # Example for SX
                # ['Z', 'A24', 'A14']
                # ['H1', 'H03', 'H2', 'H03', 'H3', 'H03', 'H4', 'H03', 'H5', 'H04', 'H6', 'H04', 'H7', 'H04', 'H8', 'H04']

                # TODO: Depending of the Machine type update the coresponding current tools dictionary

                print(items)
                items = []

    # print(total_tools_change_time/3.6e+6) # print the total tool change time in hours


machineType()
current_tools()

file.close()
output_file.close()
