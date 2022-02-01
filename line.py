# line.py


def point_on_line(a,b,c):
    m = (b[1]-a[1])/(b[0]-a[0])
    B = a[1]-m*a[0]
    y = m*c + B
    return y