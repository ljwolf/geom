import math
from point import *

def pip_cross(point, pgon):
    """
    Determines whether a point is in a polygon. Code adopted
    from the C program in Graphics Gems IV by Haines (1994).

    Input
      pgon: a list of points as the vertices for a polygon
      point: the point

    Ouput
      Returns a boolean value of True or False and the number
      of times the half line crosses the polygon boundary

    History
       October 2015. A bug in previous code, pip_cross0, is fixed.
    """
    tx, ty = point.x, point.y
    pgonx = pgon
    if pgon[0] <> pgon[-1]:
        pgonx.append(pgon[0])
    N = len(pgonx)
    crossing = 0
    inside_flag = 0
    for i in range(N-1):
        p1, p2 = pgonx[i], pgonx[i+1]
        yflag1 = (p1.y >= ty)                  # p1 on or above point
        yflag2 = (p2.y >= ty)                  # p2 on or above point
        if yflag1 != yflag2:                   # p1 & p2 on two sides of half line
            xflag1 = (p1.x >= tx)              # left-right side of p1
            xflag2 = (p2.x >= tx)              # left-right side of p2
            if xflag1 == xflag2:               # p1 & p2 on same left/right side of point
                if xflag1:
                    crossing += 1
                    inside_flag = not inside_flag
            else:                              # compute intersection
                m = p2.x - float((p2.y-ty))* (p1.x-p2.x)/(p1.y-p2.y)
                if m >= tx:
                    crossing += 1
                    inside_flag = not inside_flag
        yflag1 = yflag2
    return inside_flag, crossing

def pip_cross0(point, pgon):
    """
    Determines whether a point is in a polygon. Code adopted
    from the C program in Graphics Gems IV by Haines (1994).

    Input
      pgon: a list of points as the vertices for a polygon
      point: the point

    Ouput
      Returns a boolean value of True or False and the number
      of times the half line crosses the polygon boundary
    """
    numvert = len(pgon)
    tx=point.x
    ty=point.y
    p1 = pgon[numvert-1]                       # p1: first end point of edge
    p2 = pgon[0]                               # p2: second end point of edge
    yflag1 = (p1.y >= ty)                      # p1 on or above point
    crossing = 0
    inside_flag = 0
    for j in range(numvert-1):
        yflag2 = (p2.y >= ty)                  # p2 on or above point
        if yflag1 != yflag2:                   # p1 & p2 on two sides of half line
            xflag1 = (p1.x >= tx)              # left-right side of p1
            xflag2 = (p2.x >= tx)              # left-right side of p2
            if xflag1 == xflag2:               # p1 & p2 on same left/right side of point
                if xflag1:
                    crossing += 1
                    inside_flag = not inside_flag
            else:
                m = p2.x - float((p2.y-ty))*\
                    (p1.x-p2.x)/(p1.y-p2.y)    # compute intersection
                if m >= tx:
                    crossing += 1
                    inside_flag = not inside_flag
        yflag1 = yflag2
        p1 = p2
        p2 = pgon[j+1]
    return inside_flag, crossing

if __name__ == "__main__":
    points = [ [0,10], [5,0], [10,10], [15,0], [20,10],
               [25,0], [30,20], [40,20], [45,0], [50,50],
               [40,40], [30,50], [25,20], [20,50], [15,10],
               [10,50], [8, 8], [4,50], [0,10] ]
    ppgon = [Point(p[0], p[1]) for p in points ]
    pts = [Point(10, 30), Point(10, 20),
           Point(20, 40), Point(5, 40)]
    for p in pts:
        result = pip_cross(p, ppgon)
        if result[0] == True:
            print "Point", p, "is IN"
        else:
            print "Point", p, "is OUT"
