def getMinDistFromPoint(start, end, point):
    a = start[0]-end[0]
    b = start[1]-end[1]
    
    if a == 0:
        a = 0.0001
    if b == 0:
        b = 0.001
    
    pm = -a/b
    pc = -pm*point[0]+point[1]
    
    print(pm, pc)

    m = -1/pm
    c = -m*start[0]+start[1]
    
    print(m, c)

    ix = (pc-c)/(m-pm)
    iy = ix*m+c

    # Dist from point to line if end points did not exist
    dl = ((ix-point[0])**2+(iy-point[1])**2)**0.5

    # Perpendicular line between point and segment exists...
    print(ix, iy)
    if (start[0] <= ix <= end[0] or end[0] <= ix <= start[0]) and (start[1] <= iy <= end[1] or end[1] <= iy <= start[1]):
        return round(dl,1)
    
    print("circ")
    # Otherwise return dist between point and line end points
    return min(((start[0] - point[0])**2 + (start[1] - point[1])**2)**0.5, ((end[0] - point[0])**2 + (end[1] - point[1])**2)**0.5)

def getIntersection(start1, end1, start2, end2):
    # compute slopes and y-intercepts
    
    if start1[0] - end1[0] == 0:
        m1 = (start1[1]-end1[1])/((start1[0] + 0.0001) - end1[0])

    else:
        m1 = (start1[1]-end1[1])/((start1[0]) - end1[0])

    if start2[0] - end2[0] == 0:
        m2 = (start2[1]-end2[1])/((start2[0] + 0.0001) - end2[0])

    else:
        m2 = (start2[1]-end2[1])/((start2[0]) - end2[0])

    c1 = start1[1]-m1*start1[0]
    c2 = start2[1]-m2*start2[0]
    # intercept coordinates

    if m1 - m2 == 0:
        m1 += 0.0001

    ix = (c2-c1)/(m1-m2)
    iy = m1*ix+c1

    # See if intersection lies inside segment
    if (start1[0] <= ix <= end1[0] or end1[0] <= ix <= start1[0]) and (start1[1] <= iy <= end1[1] or end1[1] <= iy <= start1[1]) and (start2[0] <= ix <= end2[0] or end2[0] <= ix <= start2[0]) and (start2[1] <= iy <= end2[1] or end2[1] <= iy <= start2[1]):
        return (ix,iy)


        
    return None

def distance(x1, x2, y1, y2):
    return ((x1-x2) ** 2 +(y1-y2) ** 2)**0.5

def getIntersectionFromClosestEdge(edges, ray):
    minDist = 100000000
    nearestIntersection = (0, 0)
    # For an edge
    for e in edges:
        i = getIntersection(e[0], e[1], ray[0], ray[1])

        if i:

            dist = distance(i[0], i[1], ray[0][0], ray[0][1])
            if dist < minDist:
                minDist = dist
                nearestIntersection = i

    # Return intersection with nearest point
    return nearestIntersection
        