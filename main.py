import pgzrun
import numpy

WIDTH = 600
HEIGHT = 550
m1 = 1
m2 = 1
m3 = 1
v1 = numpy.array([50, -50])
v2 = numpy.array([50, 50])
v3 = numpy.array([-50, -50])
p1 = numpy.array([300, 150])
p2 = numpy.array([150, 400])
p3 = numpy.array([450, 400])
G = 15000000
MIN_R = 40.0

def draw():
    screen.clear()
    screen.draw.filled_circle(p1, 25.0, (150, 0, 0))
    screen.draw.filled_circle(p2, 25.0, (0, 150, 0))
    screen.draw.filled_circle(p3, 25.0, (0, 0, 150))

def update(dt):
    global p1,v1,p2,v2,p3,v3
    p1 = p1 + dt * v1
    p2 = p2 + dt * v2
    p3 = p3 + dt * v3
    r12 = max(MIN_R, numpy.linalg.norm(p2 - p1))
    r13 = max(MIN_R, numpy.linalg.norm(p3 - p1))
    r23 = max(MIN_R, numpy.linalg.norm(p2 - p3))
    f12 = G * m1 * m2 * (p2 - p1) / pow(r12, 3)
    f13 = G * m1 * m3 * (p3 - p1) / pow(r13, 3)
    f23 = G * m2 * m3 * (p3 - p2) / pow(r23, 3)
    v1 = v1 + dt * (f12 + f13) / m1
    v2 = v2 + dt * (-f12 + f23) / m2
    v3 = v3 + dt * (-f23 + -f13) / m3

pgzrun.go()
