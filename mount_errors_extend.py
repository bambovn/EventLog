

# my19n077.elg - event log file from old MY Series
# my200-10n0111.elg - event log file from new platform
# machine types can be DX (dual x - wagon) or SX (single x - wagon)

machine_type = ''
dx_machine_type = ['H1L', 'H2L', 'H2L', 'H4L', 'H5L', 'H6L', 'H7L', 'H8L',
                   'H1R', 'H2R', 'H3R', 'H4R', 'H5R', 'h5R', 'H7R', 'H8R']

error_stats = {}


file = open('C:\my19n077.elg')
#file = open('C:\my200-10n0111.elg')


def machineType():

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


def errors_by_head():

    for line in file:
        line = line.strip('\n').split(';')

        if line[0] == 'ME2':
            # ME2;<date-and-time>;<error-type>;<feeder-index>;<mount-head> - error line syntax
            if line[-1] not in error_stats:
                error_stats[line[-1]] = 1
            else:
                error_stats[line[-1]] += 1

        else:
            continue


def report():

    for key, value in sorted(error_stats.items()):
        print(f'{key} - {value}')


machineType()
errors_by_head()
report()


file.close()
