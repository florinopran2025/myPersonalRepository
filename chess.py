

class table:

    
    def __init__(self):
        
        columns=["A","B","C","D","E","F","G","H"]
        for i in range



class Pieces: # keeps all the pieces
    def __init__(self,color,place):
        """All pieces have a color and a place"""
        self.color=color # black/white
        self.place=place # place (should be a tuplet)


class Pawns(Pieces):    
    def __init__(self,color,place,everMoved):
        super().__init__(color,place)
        self.everMoved=everMoved # True/False
        moveOptions=[(place[0]+1,place[1])]
        if self.everMoved=="False":
            self.moveOptions.append()







