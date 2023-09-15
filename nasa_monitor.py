from rover import Rover

occupied_positions = list()  # Keep track of occupied positions
def process_instructions(rover, new_instructions, plateau_size):
    """
    Modifies and checks the variables needed to move the rover around the plateau.

    :param rover: Contains a Rover object. This object is the one to be modified.
    :param new_instructions: String containing the instructions to move the rover
    :param plateau_size: Tuple of ints containing the size of the plateau
    :return: boolean. 1 To continue moving the rover, 0 to end the movement.
    """
    backforward = 1 # Flag to know if more instructions are entered by the user.
    while backforward:
        instructions = new_instructions
        for instruction in instructions:
            if instruction == 'L':
                rover.rotate_left()
            elif instruction == 'R':
                rover.rotate_right()
            elif instruction == 'M':
                rover.move()
                backforward = 0
                if rover.x > plateau_size[0] or rover.y > plateau_size[1] or rover.x < 0 or rover.y < 0:
                    rover.moveBackward()
                    backforward = 1
                    new_instructions = input(f'Rover is going out of the plateau. Please, enter new instructions separated '
                                         f'by spaces. Rover position: ({rover.x}, {rover.y}) {rover.heading}')
                    break
    rover_coordinates = (rover.x, rover.y)
    # Check if the final position of the rover matches with another rover.
    if rover_coordinates in occupied_positions:
        rover_stepped_on = occupied_positions.index(rover_coordinates)
        choice_ok = 1
        while choice_ok:
            step_on = input(
                f'Hey! Rover {rover_stepped_on} is in your final position {rover_coordinates} {rover.heading}. Do you want to share position with Rover {rover_stepped_on}? (Y/N)')
            if step_on == 'N' or step_on == 'n':
                return 1
            elif step_on == 'Y' or step_on == 'y':
                return 0
            else:
                choice_ok = 1

def check_position(coordinates, rover_heading, plateau_x, plateau_y):
    """
    Checks the initial position entered by the user.

    :param coordinates: Tuple containing the coordinates (x,y) of the rover
    :param rover_heading: Character containing the heading of the rover
    :param plateau_x: Integer to refer to the maximum plateau width
    :param plateau_y: Integer to refer to the maximum plateau height
    :return: Boolean. 1 if the position checked is correct, 0 for the opposite
    """
    if coordinates[0] > plateau_x or coordinates[1] > plateau_y:
        return 1
    if rover_heading != 'N' and rover_heading != 'S' and rover_heading != 'W' and rover_heading != 'E':
        return 1
    else:
        return 0
def nasa_monitor():
    """
    Main function.
    :return: void
    """
    plateau_size_str = input("Enter plateau size: ").split()
    plateau_x, plateau_y = map(int,plateau_size_str)
    plateau_size=(plateau_x,plateau_y)

    while True:
        try:
            rover_position = input("Enter rover position and heading: ").split()
            rover_x, rover_y, rover_heading = rover_position
            coordinates = (int(rover_x), int(rover_y))

            # Check the position entered by the user.
            incorrect_position = check_position(coordinates, rover_heading,plateau_x, plateau_y)
            if incorrect_position:
                print(f'Please, enter a valid position and heading inside the plateau ({plateau_x}, {plateau_y}):')
                continue

            rover = Rover(coordinates, rover_heading)
            if coordinates in occupied_positions:
                rover_stepped_on = occupied_positions.index(coordinates)
                step_on = input(
                    f'Hey! Rover {rover_stepped_on} is in your inicial position {coordinates}. Do you want to share position with Rover {rover_stepped_on}? (Y/N)')
                if step_on == 'N' or step_on == 'n':
                    continue

            more_moves = 1
            while more_moves:
                instructions = input("Enter rover instructions separated by spaces: ")
                more_moves = process_instructions(rover, instructions, plateau_size)

            print(f"Rover's final position and heading: {rover.x} {rover.y} {rover.heading}")
            occupied_positions.append((rover.x, rover.y))


        except ValueError:
            print("Invalid input format. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    nasa_monitor()
