class Node:
    END_OF_TEXT = chr(3)

    def __init__(self) -> None:
        """
        Initialization of an empty node
        """
        self.sons = {}

    def append(self, sequence: str) -> int:
        """
        Add recursively a sequence of characters : one character per node.
        The end of this sequence is indicated with a node END_OF_CHARACTER that doesn't have sons.
        """

        if len(sequence) == 0:  # If end of sequence, create END_OF_CHARACTER node
            self.sons[Node.END_OF_TEXT] = None
        else:  # Else, find or create a node named with the first character, then add to it the rest of sequence
            if not sequence[0] in self.sons:
                self.sons[sequence[0]] = Node()

            self.sons[sequence[0]].append(sequence[1:])

    def isPrefixIn(self, sequence: str) -> int:
        """
        Search recursively if the first characters of sequence is in tree.
        If it is, returns the number of character, else returns -1
        """
        if Node.END_OF_TEXT in self.sons:
            return 0

        if len(sequence) > 0 and sequence[0] in self.sons:
            next = self.sons[sequence[0]].isPrefixIn(sequence[1:])
            
            return next + (next >= 0)  # (next >= 0) is used to avoid incrementing -1
        else:
            return -1