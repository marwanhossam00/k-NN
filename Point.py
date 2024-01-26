import math

class Point:
    """
    Represents a point in two-dimensional geometric coordinates

    p_1 = Point()
    p_2 = Point(3,4)
    p_1.calculate_distance(p_2)
    5.0
    """
    def __init__(self, x:float = 0, y:float = 0) -> None:
        """
        Initializes the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin.

        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.move(x,y)

    def move(self, x: float, y: float)-> None:
        """
        Move the point to a new location in 2D space

        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self)->None:
        """
        Reset the point to the origin
        """
        self.move(0,0)

    def calculate_distance(self, other:"Point")-> float:
        """
        Calculate the Euclidean distance from this point to another point
        passed as a parameter

        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x-other.x,self.y-other.y)