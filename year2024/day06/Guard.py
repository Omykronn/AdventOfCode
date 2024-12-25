class Guard:
    def __init__(self, position: (int, int), facing_direction: (int, int)):
        """
        Initialize the position and the direction of the guard
        """

        self.position = position
        self.facing_direction = facing_direction

    def turnRight(self):
        """
        Set the direction after turning right
        """

        self.facing_direction = (self.facing_direction[1], -self.facing_direction[0])

    def getForwardPosition(self):
        """
        Return the position in front of the guard
        """

        return (self.position[0] + self.facing_direction[0], self.position[1] + self.facing_direction[1])

    def next(self, matrix: [str]):
        """
        Set next position and direction of the guard
        """

        forward_position = self.getForwardPosition()

        if 0 <= forward_position[0] < len(matrix) and 0 <= forward_position[1] < len(matrix[forward_position[0]]) and matrix[forward_position[0]][forward_position[1]] == "#":
            self.turnRight()
            self.position = self.getForwardPosition()
        else:
            self.position = forward_position