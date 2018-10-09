# Notation Key:
#
# Positions -
# Top Front Left Corner, 1
# Top Front Right Corner, 2
# Top Back Right Corner, 3
# Top Back Left Corner, 4
# Bottom Back Left Corner, 5
# Bottom Front Left Corner, 6
# Bottom Front Right Corner, 7
# Bottom Back Right Corner, 8
#
# Cube State Notation -
# Sub arrays represent different cubies, sub array indexes are positions
# Sub array = [Position in solved state, Orientation*]
# *For orientation, 0 means the Yellow or White is facing up or down, 1 means the Yellow/White is rotated once clockwise
#  from facing up/down, 2 means the Yellow/White is rotated twice clockwise
#
# Note: The algorithm uses a method used in blind fold cubing, so it is not the fastest

print("Key:")
print("R - turn right face clockwise, R' - turn right face counterclockwise")
print("L - turn left face clockwise, L' - turn left face counterclockwise")
print("U - turn up face clockwise, U' - turn down face counterclockwise")
print("D - turn down face clockwise, D' - turn down face counterclockwise")
print("F - turn front face clockwise, F' - turn front face counterclockwise")
print("B - turn back face clockwise, B' - turn back face counterclockwise")
print("x - turn cube around x-axis clockwise, x' - turn cube around x-axis counterclockwise")
print("y - turn cube around y-axis clockwise, y' - turn cube around y-axis counterclockwise")
print("z - turn cube around z-axis clockwise, z' - turn cube around z-axis counterclockwise")

print("")

print("Instructions:")


# functions corresponding with set-up moves to re-define position of corners after the cube is turned
def format_cube(turn_direction, cubie_permutation_index):
    if turn_direction == 0:
        return cubie_permutation_index
    elif turn_direction == 1:
        return rotate_cube_z(cubie_permutation_index)
    elif turn_direction == 2:
        return rotate_cube_z(rotate_cube_z(cubie_permutation_index))
    elif turn_direction == 3:
        return rotate_cube_z(rotate_cube_z(rotate_cube_z(cubie_permutation_index)))
    elif turn_direction == 4:
        return rotate_cube_x(rotate_cube_x(cubie_permutation_index))
    elif turn_direction == 5:
        return rotate_cube_x(rotate_cube_x(rotate_cube_z(cubie_permutation_index)))
    elif turn_direction == 6:
        return rotate_cube_y(rotate_cube_y(cubie_permutation_index))
    elif turn_direction == 7:
        return rotate_cube_y(rotate_cube_y(rotate_cube_z(cubie_permutation_index)))


# re-definition of corner positions after cube is rotated around the x-axis
def rotate_cube_x(integer):
    if integer == 0:
        return 3
    elif integer == 1:
        return 2
    elif integer == 2:
        return 7
    elif integer == 3:
        return 4
    elif integer == 4:
        return 5
    elif integer == 5:
        return 0
    elif integer == 6:
        return 1
    elif integer == 7:
        return 6


# re-definition of corner positions after cube is rotated around the y-axis
def rotate_cube_y(integer):
    if integer == 0:
        return 1
    elif integer == 1:
        return 6
    elif integer == 2:
        return 7
    elif integer == 3:
        return 2
    elif integer == 4:
        return 3
    elif integer == 5:
        return 0
    elif integer == 6:
        return 5
    elif integer == 7:
        return 4


# re-definition of corner positions after cube is rotated around the z-axis
def rotate_cube_z(integer):
    if integer == 0:
        return 3
    elif integer == 1:
        return 0
    elif integer == 2:
        return 1
    elif integer == 3:
        return 2
    elif integer == 4:
        return 7
    elif integer == 5:
        return 4
    elif integer == 6:
        return 5
    elif integer == 7:
        return 6


# main function
def solve_2x2x2_cube(cube_state):

    # initial set-up move: how to turn cube in order for a corner to be in position 1 for algorithm
    # index corresponds with the position the cubie is currently in
    set_up_a = ["", "z ", "z2 ", "z' ", "x2 ", "z x2 ", "y2 ", "z y2 "]

    # inverse moves corresponding with set_up moves
    set_up_a_inverse = ["", "z' ", "z2 ", "z ", "x2 ", "x2 z' ", "y2 ", "y2 z' "]

    # secondary set-up move: sequence of face turns to move any cubie into position 2 for algorithm
    # index corresponds with the position the cubie is currently in
    set_up_b = ["", "", "B' U' B U ", "B2 R2 ", "D' R2 ", "D2 R2 ", "D R2 ", "R2 "]

    # inverse moves corresponding with set_up moves
    set_up_b_inverse = ["", "", "U' B' U B ", "R2 B2 ", "R2 D ", "R2 D2 ", "R2 D' ", "R2 "]

    # algorithm which turns the cubie in position 1 clockwise and the cubie in position 2 counterclockwise
    orientation_algorithm = "U R U R' U R U2 R' L' U' L U' L' U2 L U' "

    # algorithm which swaps the cubie's in positions 1 and 2
    permutation_algorithm = "R' F R' B2 R F' R' B2 R2 U' "

    # initialization of an array of the pairs of cubies oriented together
    orientation_pairs = []

    # initialization of an array of the cubies in orientation 1 in a pair
    positions_a = []

    # initialization of an array of the cubies in orientation 2 in a pair
    positions_b = []

    # initialization of a searching index
    orientation_index_a = 0

    # initialization of a searching index
    orientation_index_b = 0

    # finding the total number of cubies in orientation 1 and 2 separately as count_a and count_b respectively
    count_a = 0
    count_b = 0
    for a in range(0, len(cube_state)):
        if cube_state[a][1] == 1:
            count_a += 1
        elif cube_state[a][1] == 2:
            count_b += 1

    # process of identifying the pairs of cubies in orientation 1 and 2
    while orientation_index_a < len(cube_state) and orientation_index_b < len(cube_state):

        # identifies orientation 2 cubies
        if cube_state[orientation_index_a][1] == 2:
            while orientation_index_b < len(cube_state):

                # identifies orientation 1 cubies
                if cube_state[orientation_index_b][1] == 1:
                    positions_b.append(orientation_index_a)
                    positions_a.append(orientation_index_b)

                    # once a pair is identified, they are added to the array and the search continues
                    orientation_pairs.append([orientation_index_a, orientation_index_b])
                    orientation_index_b += 1
                    break
                orientation_index_b += 1
        orientation_index_a += 1

    # deals with the situation in which there are more 1 orientation cubies that 2 orientation cubies
    if count_a > count_b:

        # initializes search indexes
        orientation_index_a = 0
        orientation_index_b = 0
        c = 0

        # process of identifying matches of three 1 orientation cubies to one 0 orientation cubie
        while orientation_index_a < len(cube_state) and orientation_index_b < len(cube_state):

            # identifies a 0 orientation cubie
            if cube_state[orientation_index_a][1] == 0:
                while orientation_index_b < len(cube_state):

                    # identifies 1 orientation cubies
                    if cube_state[orientation_index_b][1] == 1:

                        # filters out 1 orientation cubies already in a pair
                        bol = False
                        for x in range(0, len(positions_a)):
                            if positions_a[x] == orientation_index_b:
                                bol = True
                                orientation_index_b += 1
                                break
                        if bol:
                            break

                        # pairs are appended and the search continues
                        orientation_pairs.append([orientation_index_a, orientation_index_b])
                        c += 1
                        orientation_index_b += 1
                        break
                    orientation_index_b += 1

            # the search is over once the number of pairs exceed the maximum possible
            if c >= count_a - len(positions_a):
                break

            # once a 0 orientation cubie has three 1 orientation cubie, another 0 orientation cubie is found
            if c == 3:
                orientation_index_b += 1

    # deals with the situation in which there are more 2 orientation cubies that 1 orientation cubies
    elif count_b > count_a:

        # initializes search indexes
        orientation_index_a = 0
        orientation_index_b = 0
        c = 0

        # process of identifying matches of three 2 orientation cubies to one 0 orientation cubie
        while orientation_index_a < len(cube_state) and orientation_index_b < len(cube_state):

            # identifies a 0 orientation cubie
            if cube_state[orientation_index_a][1] == 0:
                while orientation_index_b < len(cube_state):

                    # identifies 2 orientation cubies
                    if cube_state[orientation_index_b][1] == 2:

                        # filters out 1 orientation cubies already in a pair
                        bol = False
                        for x in range(0, len(positions_a)):
                            if positions_b[x] == orientation_index_b:
                                bol = True
                                orientation_index_b += 1
                                break
                        if bol:
                            break

                        # pairs are appended and the search continues
                        orientation_pairs.append([orientation_index_b, orientation_index_a])
                        c += 1
                        orientation_index_b += 1
                        break
                    orientation_index_b += 1

            # the search is over once the number of pairs exceed the maximum possible
            if c >= count_b - len(positions_b):
                break

            # once a 0 orientation cubie has three 2 orientation cubie, another 0 orientation cubie is found
            if c == 3:
                orientation_index_b += 1

    # prints instructions for orienting corners for each pair
    for index in range(0, len(orientation_pairs)):

        # initial and secondary set up moves
        print(set_up_a[orientation_pairs[index][0]], end="")
        print(set_up_b[format_cube(orientation_pairs[index][0], orientation_pairs[index][1])], end="")

        # directs to orientation algorithm
        print(orientation_algorithm, end="")

        # reverses both set up moves
        print(set_up_b_inverse[format_cube(orientation_pairs[index][0], orientation_pairs[index][1])], end="")
        print(set_up_a_inverse[orientation_pairs[index][0]])

    # identifies which corners are already in the correct permutation
    correct_indexes = []
    for index in range(0, len(cube_state)):
        if cube_state[index][0] - 1 == index:
            correct_indexes.append(index)

    # initializes the array of fixing maps
    fixing_maps = [[0]]

    # initializes the index for the current fixing map
    total_fixing_index = 0

    # initializes the total amount of elements in all fixing maps
    total_fixing_number = 0

    # initializes indexes
    temp_index = 0
    new_index = 0

    # process of calculating fixing maps
    while total_fixing_number < 8 - (2 * total_fixing_index) - len(correct_indexes):

        # when a fixing map exists, searches for the first index not included
        if total_fixing_index != 0:
            for integer in range(0, len(cube_state)):
                for n in range(0, len(fixing_maps)):

                    # searches through each previous fixing map for a match
                    for index in range(0, len(fixing_maps[n])):

                        # if a match to the index in question comes up, move on to the next integer
                        bol = False
                        if fixing_maps[n][index] == integer:
                            bol = True
                            break
                    if bol:
                        break

                # action when no match is found
                else:

                    # state the initial position of the index used to calculate the fixing map
                    new_index = integer
                    fixing_maps.append([new_index])
                    temp_index = new_index
                    break

        # finds the rest of the fixing map from the initial position
        while True:

            # adds next element of fixing map, updates index
            fixing_maps[total_fixing_index].append(cube_state[temp_index][0] - 1)
            temp_index = cube_state[temp_index][0] - 1

            # once the fixing map loops onto itself, exit while loop
            if temp_index == new_index:
                del fixing_maps[total_fixing_index][len(fixing_maps[total_fixing_index]) - 1]
                break

        # updates index for next loop
        total_fixing_index += 1

        # updates total amount of indexes in all fixing maps
        count = 0
        for x in range(0, len(fixing_maps)):
            for y in range(len(fixing_maps[x])):
                count += 1
        total_fixing_number = count

    # prints instructions for swapping corners with each fixing map
    for index in range(0, len(fixing_maps)):

        # initializes index at which the swapping starts
        swap_index = len(fixing_maps[index]) - 1

        # works backwards at the fixing map
        while swap_index > 0:

            # initial and secondary set-up moves
            print(set_up_a[fixing_maps[index][swap_index - 1]], end="")
            print(set_up_b[format_cube(fixing_maps[index][swap_index - 1], fixing_maps[index][swap_index])], end="")

            # algorithm to swap the top front two corners
            print(permutation_algorithm, end="")

            # reverses set-up moves
            print(set_up_b_inverse[format_cube(fixing_maps[index][swap_index - 1], fixing_maps[index][swap_index])], end="")
            print(set_up_a_inverse[fixing_maps[index][swap_index - 1]])

            # updates swap_index
            swap_index -= 1


# defining the permutation and orientation of the the cubies on a scrambled cube
# ex: [[3, 2]... means that the third cubie is in the first position (3) is oriented with the white/yellow
# side rotated twice clockwise (see cube state notation above)
test_state = [[3, 0], [5, 1], [4, 0], [6, 0], [1, 1], [8, 1], [7, 1], [2, 2]]

# input to the main function
solve_2x2x2_cube(test_state)
