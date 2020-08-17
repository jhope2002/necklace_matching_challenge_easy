def same_necklace(necklace_one, necklace_two):

    is_same_necklace = False
    repeats = 0

    if len(necklace_one) != len(necklace_two):
        is_same_necklace = False   

    else:
        necklace_two_shifted = necklace_two
        for i in range(len(necklace_one)):
            necklace_two_shifted = necklace_two_shifted[1:] + necklace_two_shifted[0]
            # print(necklace_two_shifted)
            if necklace_one == necklace_two_shifted:
                is_same_necklace = True
                repeats += 1

    if is_same_necklace == False:
        print('This is not the same necklace.')

    elif is_same_necklace == True and repeats == 1:
        print(f'This is the same necklace. It repeats just {repeats} time.')
    
    elif is_same_necklace == True and repeats > 1:
        print(f'This is the same necklace. It repeats {repeats} times.')
            
            


#same_necklace('nicole', 'nicolette') # Necklaces of different length
#same_necklace('nicole', 'nicole') # Necklace is identical
#same_necklace('nicole', 'icolen') # Same Necklace, No repeats
#same_necklace('abcabcabc', 'bcabcabca') # Same necklace, 3 repeats