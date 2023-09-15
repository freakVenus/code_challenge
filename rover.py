class Rover:
    """
    Class Rover used to identify the rovers in the service.
    """
    def __init__(self, coordinates, heading):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.heading = heading

    def move(self):
        """
        Modifies the variables to move the rover forward.
        :return: void.
        """
        if self.heading == 'N':
            self.y += 1
        elif self.heading == 'S':
            self.y -= 1
        elif self.heading == 'E':
            self.x += 1
        elif self.heading == 'W':
            self.x -= 1

    def moveBackward(self):
        """
        Modifies the variables to move the rover backward.
        :return: void.
        """
        if self.heading == 'N':
            self.y -= 1
        elif self.heading == 'S':
            self.y += 1
        elif self.heading == 'E':
            self.x -= 1
        elif self.heading == 'W':
            self.x += 1

    def rotate_left(self):
        """
        Modifies the variables to rotate the rover to the left.
        :return: void.
        """
        if self.heading == 'N':
            self.heading = 'W'
        elif self.heading == 'S':
            self.heading = 'E'
        elif self.heading == 'E':
            self.heading = 'N'
        elif self.heading == 'W':
            self.heading = 'S'

    def rotate_right(self):
        """
        Modifies the variables to rotate the rover to the right.
        :return: void.
        """
        if self.heading == 'N':
            self.heading = 'E'
        elif self.heading == 'S':
            self.heading = 'W'
        elif self.heading == 'E':
            self.heading = 'S'
        elif self.heading == 'W':
            self.heading = 'N'
