from math import *


def initOxy(pen, width, height, unit):
    ''' Draw Cartesian orthogonal system Oxy

    Argvs: pen - turtle object
           width - lenght of Ox
           height - lenght of Oy
           unit - pixels correspond with 1 unit in Ox
    '''
    drawAxis(pen, width, unit)
    pen.lt(90)
    drawAxis(pen, height, unit)
    pen.lt(180)
    drawAxis(pen, width, unit, False)
    pen.rt(90)
    drawAxis(pen, height, unit, False)


def drawAxis(pen, lenght, unit, positive=True):
    ''' Draw a axis (Ox/ Oy)

    Argvs: positive - draw arrow
    '''
    for i in range(int(lenght)):
        pen.fd(unit)
        numPoint(pen)
    pen.fd(unit / 2)
    if positive:
        pen.lt(135)
        pen.fd(unit / 5.5)
        pen.bk(unit / 5.5)
        pen.lt(90)
        pen.fd(unit / 5.5)
    pen.pu()
    pen.home()
    pen.pd()


def numPoint(pen):
    ''' Draw point mark number point'''
    pen.lt(90)
    pen.fd(1.5)
    pen.bk(3)
    pen.fd(1.5)
    pen.rt(90)


def makeLine(func, width, height, unit):
    '''Make a list of pair (x, y), return lines'''
    line = [[]]
    index = 0
    step = 1 / unit
    preDis = 0

    if not isValid(width, func):
        raise ArithmeticError('Invalid Function!')

    step = 1 / 20
    for x in range(int(-width / step), int(width / step)):
        x = x * step
        try:
            y = execute(func, x)
            if y > height or y < -height:
                continue

            if preDis != 0:
                currentDis = dis((x, y), (x - step, execute(func, x - step)))
                if currentDis > 10 * preDis:
                    line.append([])
                    index += 1
                preDis = currentDis

            line[index].append((x * unit, y * unit))
        except:
            line.append([])
            index += 1

    return line


def dis(point1, point2):
    ''' Return a distance between 2 points'''
    res = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    return sqrt(res)


def execute(func, x):
    ''' Execute function with argv x'''
    func = func.replace('func', str(x))
    y = eval(func)
    return y


def isValid(width, func):
    ''' Check func is valid??'''
    for x in range(int(-width), int(width)):
        try:
            execute(func, x)
            return True
        except:
            pass
    return False
