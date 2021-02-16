import math

xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35

xa = -36
ya = 97

xb = .34
yb = .91

def calculate_distance():
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

def calcualte_length():
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

distance = calculate_distance()
length = calcualte_length()
print('distance', distance)
print('length', length)