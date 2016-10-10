def funcioncilla_multiple(b,c="patata",d=27):
    """funcioncilla ejemplo """
    b = b +3 + d
    return b-2,c+" fritas"

PATATAS=["variable","capitalize means by convection constant"]

class AnimalImage():
    def __init__(self,path_to_image):
        self.path_to_image = path_to_image
    def animal(self): # method and functions names tend to be not capitalized
        if 'dog' in self.path_to_image:
            return 'dog'
        if 'cat' in self.path_to_image:
            return 'cat'
