# Globals
import re
REGEX = r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def valid_cc(input_num):
    ### Returns true if valid CC number
    #It must start with a 4, 5 or 6 
    #It must contain exactly 16 digits
    #It must only consist of digits (0-9)
    #It may have digits in groups of 4, separated by one hyphen "-"
    #It must NOT use any other separator like ' ' , '_', etc. 
    ###

    groups = re.match(REGEX, input_num)
    if not groups:
        return False
    if input_num.count('-') not in (0, 3):
        return False
    return repeats(''.join(groups.groups()))

def repeats(cc):
    # Determine if there are 4 or more consecutive numbers
    for i, j in enumerate(cc):
        try:
            if (cc[i],
                cc[i+1],
                cc[i+2],
                cc[i+3]
            ) == (j, j, j, j):
                return False
        except IndexError:
            pass
    return True

if __name__ == '__main__':
    # Main - do the work

    # Get number of CCs to check
    total_ccs = int(input())

    # Store CCs to list
    ccs = [
        input()
        for count in range(total_ccs)
    ]

    # Test each CC num
    for cc in ccs:
        if valid_cc(cc):
            print('Valid')
        else:
            print('Invalid')
