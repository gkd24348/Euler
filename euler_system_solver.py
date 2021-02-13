import numpy as np

start = 0
end = 0.5
step = 0.1

y0 = -1
z0 = 0

def yd(x, z):
    return 4 * x + z * z
    
def zd(x, y):
    return - 5 * x + y * y

############################################################

x = np.arange(start, end, step)

print(x)

prev_y = y0
prev_z = z0

for curr_x in x:

    prev_yd = yd(curr_x, prev_z)
    prev_zd = zd(curr_x, prev_y)

    prev_y = prev_y + prev_yd * step
    prev_z = prev_z + prev_zd * step

    print(curr_x + 0.1, "y=", prev_y, "\ty\'=", prev_yd, "\tz=", prev_z, "\tz\'=", prev_zd)