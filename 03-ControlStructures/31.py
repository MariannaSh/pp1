x=int(input())
y=int(input())
if x>0 and y>0:
    print(f'Point P({x,y}) is in the first quadrant of the coordinate system')
elif x<0 and y>0:
    print(f'Point P({x,y}) is in the second quadrant of the coordinate system')
elif x<0 and y<0:
    print(f'Point P({x,y}) is in the third quadrant of the coordinate system')
elif x>0 and y<0:
    print(f'Point P({x,y}) is in the fours quadrant of the coordinate system')
else:
    print('position (0,0)')