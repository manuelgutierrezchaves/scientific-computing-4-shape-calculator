class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            i = 0
            str = ""
            while i < self.height:
                j = 0

                while j < self.width:
                    str = str + "*"
                    j += 1
                str = str + "\n"
                i += 1

        return(str)

    def get_amount_inside(self,instance):
        ver = int(self.width / instance.width)
        hor = int(self.height / instance.height)
        return ver * hor

class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self,new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self,new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self,new_side):
        self.width = new_side
        self.height = new_side
