# Reading EventLog file from Mycronic Pick and Place machine and returning number of errors

def mountErrors():

    # Loading the Eventlog file
    file = open(r"log_files\new.elg")

    total_error_counter = 0

    
    pick_error = 0  # Failed to pick. Attempt to pick component from magazine failed. This includes failed vacuum-test.
    mdim_error = 0  # Wrong mechanical dimension. Component mechanical dimensions not within spec.
    elve_error = 0  # Failed electrical verification.
    optc_error = 0  # Optical centering failed.
    step_error = 0  # The magazine cannot be stepped. Probably a hardware error.
    lsfe_error = 0  # Local site fiducial search failed.
    other_error = 0 # Other errors, for instance package not mountable.


    #TODO to implement detailed errors by Head (For DX left/right) Midas and Hydra
    #TODO to implement current mount tools status on error the current mount tool to be noted




    for line in file:

        splitted_line = line.split(';')

        if splitted_line[0] == "ME2":
            total_error_counter += 1
        else:
            continue

        # ME2;<date-and-time>;<error-type>;<feeder-index>;<mount-head> - error line syntax

        if splitted_line[2] == "PICK":
            pick_error +=1
        elif splitted_line[2] == "MDIM":
            mdim_error +=1
        elif splitted_line[2] == 'ELVE':
            elve_error +=1
        elif splitted_line[2] == 'OPTC':
            optc_error +=1
        elif splitted_line[2] == 'STEP':
            step_error +=1
        elif splitted_line[2] == 'LSFE':
            lsfe_error +=1
        else:
            other_error +=1
            



    file.close()

    print(f'Total errors: {total_error_counter}')
    print(f'Pick errors: {pick_error}')
    print(f'Mechanical dimensions errors: {mdim_error}')
    print(f'Electrical verification errors: {elve_error}')
    print(f'Optical centring errors: {optc_error}')
    print(f'Magazine stepper errors: {step_error}')
    print(f'Local fiducial errors: {lsfe_error}')
    print(f'Other errors: {other_error}')
    print(f'-----------------------------------------')
    print(f'Errors by mounthing head')



mountErrors()
