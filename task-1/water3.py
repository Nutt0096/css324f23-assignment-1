def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)

def successors(s):
    x, y, z = s

    if x>0 and y<5:
        if y+x <= 5:
            yield ((0,y+x,z),x)
        else:
            yield (((x-(5-y)),5,z),5-y)

    if x>0 and z<3:
        if z+x <= 3:
            yield ((0,y,z+x),x)
        else:
            yield (((x-(3-z)),y,3),3-z)

    if y>0 and x<8:
        if x+y <= 8:
            yield ((x+y,0,z),y)
        else:
            yield ((8,(y-(8-x)),z),8-x)
            
    if y>0 and z<3:
        if z+y <= 3:
            yield ((x,0,z+y),y)
        else:
            yield ((x,(y-(3-z)),3),3-z)
            
    if z>0 and x<8:
        if x+z <= 8:
            yield ((x+z,y,0),z)
        else:
            yield ((8,y,(z-(8-x))),8-x)
            
    if z>0 and y<5:
        if y+z <= 5:
            yield ((x,y+z,0),z)
        else:
            yield ((x,5,(z-(5-y))),5-y)
    
    return []
