import math

v_0 = 20.0 # in m/s
theta = 30.0 # in degrees
g = 9.8 # in m/s^2
y = 0.0 # in m 
x = 0.0 # in m

v_x0 = v_0*math.cos(theta*math.pi/180.0)
v_y0 = v_0*math.sin(theta*math.pi/180.0)
t_flight = 2.0*v_y0/g
dt = t_flight/200.0

outFile = open("projectileData.txt", "w")
v_y = v_y0
y_max = 0.0
for i in range(0,201):
    x = x + v_x0*dt
    y = y + v_y*dt - 0.5*g*dt*dt
    v_y = v_y - g*dt
    outFile.write(str(i*dt) + " " + str(x) + " " + str(y) + " " + str(v_x0) + " " + str(v_y) + "\n")
    if (y > y_max):
        y_max = y

outFile.close()
print("Maximum height:", y_max)
print("horizontal range:", x)