# Import the BaseGeometry class
from base_geometry import BaseGeometry

# Define the Rectangle class that inherits from BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate that width and height are positive integers
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        # Set the private attributes
        self.__width = width
        self.__height = height
