import turtle
import graph.module as module


class Graph:
    ''' Represent a Cartesian orthogonal system Oxy

    Attributes: width - lenght of Ox
                height - lenght of Oy
                unit - pixels correspond with 1 unit in Ox
                pen - a object of turtle class
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.unit = 250 / max(self.width, self.height)
        self.pen = turtle.Turtle()
        self.pen.hideturtle()  # hide turtle
        self.pen.speed(0)  # set max speed

        module.initOxy(self.pen, self.width, self.height, self.unit)
        # draw Cartesian orthogonal system Oxy

    color = ['red', 'blue', 'green', 'brown', 'orange']  # color of pen
    indexColor = 0

    def draw(self, func, sepLine=True):
        if sepLine:  # 2 line is not same color
            if Graph.indexColor == len(Graph.color):
                Graph.indexColor = 0
            self.pen.pencolor(Graph.color[Graph.indexColor])
            Graph.indexColor += 1

        lines = module.makeLine(func, self.width, self.height, self.unit)
        for line in lines:
            first = True
            for (x, y) in line:
                if first:  # this point is the first of a line
                    self.pen.pu()
                    self.pen.goto((x, y))
                    self.pen.pd()
                    first = False
                else:
                    self.pen.goto((x, y))


def main():
    width = turtle.numinput('INPUT WIDTH', 'Enter width: ', 10, 0, 50)
    if width is None:
        return

    height = turtle.numinput('INPUT HEIGHT', 'Enter height: ', 10, 0, 50)
    if height is None:
        return

    graph = Graph(width, height)

    while True:
        func = turtle.textinput("IMPORT FUNCTION", "Enter function: ")
        if func is None:
            break

        graph.draw(func)


if __name__ == '__main__':
    main()
