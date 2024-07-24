from toolbox.polygons import segmentIntercept


class Block:
    def __init__(self, start_coor: (int, int), end_coor: (int, int)) -> None:
        """
        Initalizes a block with the coordinates of two opposite corners
        """

        self.start_coor = start_coor
        self.end_coor = end_coor
        self.height = self.end_coor[2] - self.start_coor[2]
        self.underlist = []
        self.finalZ = 0

        self.supported = []
        self.nb_supporters = 0
        self.nb_supporters_fallen = 0
        

    def is_above(self, other) -> bool:
        """
        Test if self is above other
        """

        return self.start_coor[2] > other.end_coor[2] and segmentIntercept((self.start_coor[0], self.end_coor[0]), (other.start_coor[0], other.end_coor[0])) and segmentIntercept((self.start_coor[1], self.end_coor[1]), (other.start_coor[1], other.end_coor[1]))

    def getFinalZ(self) -> int:
        """
        Returns the final altitude after the fall
        """

        if self.finalZ == 0:
            if len(self.underlist) == 0:
                self.finalZ = 0
            else:
                for underBlock in self.underlist:
                    if underBlock.getFinalZ() + underBlock.height + 1 > self.finalZ:
                        self.finalZ = underBlock.getFinalZ() + underBlock.height + 1

        return self.finalZ

    def sayIFall(self) -> int:
        """
        Sends a flag to supported blocks and couts how many other fall
        """

        count = 1
        
        for block in self.supported:
            count += block.heFalls()

        return count

    def heFalls(self) -> int:
        """
        Checks if still have a support which didn't fall and returns the numbers of supported blocks fallen
        """

        self.nb_supporters_fallen += 1

        if self.nb_supporters_fallen == self.nb_supporters:
            return self.sayIFall()

        return 0

    def reload(self) -> None:
        """
        Reset the system : no blocks fell
        """
        self.nb_supporters_fallen = 0

        for block in self.supported:
            block.reload()

