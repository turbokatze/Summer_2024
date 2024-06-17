class Shape:
    def __init__(self, colour, square):
        self.__colour = colour
        self.__square = square
    def setcolour(self, colour):
        self.__colour = colour
    def get_colour(self):
        return self.__colour
    def setsquare(self, square):
        self.__square = square
    def get_square(self):
        return self.__square
    def info(self):
        print(f"{self.__colour}: {self.__square}")

def form():
    colour = input('Enter colour: '); square = input('Enter square: ')
    col_sq = Shape(colour, square)
    print(f'Colour is: {col_sq.get_colour()}, square is: {col_sq.get_square()}')

form()
