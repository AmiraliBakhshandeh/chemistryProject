
def Bohr(electron):
    max = [2, 8, 18, 32, 64, 128, 256]
    current_layer = 0
    temp_layer = 0
    layer = [0, 0, 0, 0, 0, 0, 0]
    in1 = electron
    while in1 > 0:
        temp_layer = current_layer+1
        if layer[current_layer] < max[current_layer]:
            if layer[current_layer] >= 8 and layer[current_layer+1] < 2:
                layer[current_layer+1] += 1
                in1 -= 1
            elif layer[temp_layer] >= 8 and layer[temp_layer+1] < 2:
                layer[temp_layer+1] += 1
                in1 -= 1
            elif layer[current_layer] >= 18 and layer[temp_layer] < 8:
                layer[current_layer+1] += 1
                in1 -= 1
            elif layer[current_layer] >= 32 and layer[temp_layer] < 18:
                layer[current_layer+1] += 1
                in1 -= 1
            elif layer[current_layer] >= 32 and layer[temp_layer+1] < 8:
                layer[temp_layer+1] += 1
                in1 -= 1
            else:
                layer[current_layer] += 1
                in1 -= 1
        else:
            current_layer += 1
    return layer



def Circle(draw,list):
    def draw_atom(pen, radius, levels, electrons_per_level, electron_size=15, electron_color="red"):
        full_circle = 360
        for level in range(levels):
            r = radius * (level + 1)                           # concentric circles
            electrons_in_level = electrons_per_level[level]
            arcs = full_circle / electrons_in_level            # arcs between each electron
            circumference = 0
            pen_jump(pen, 0, -r)                               # centering
            while circumference < full_circle:
                pen.dot(electron_size, electron_color)
                pen.circle(r, arcs)
                circumference = circumference + arcs
    electrons_per_level = []
    levels = len(list)
    first_level_radius = 25

    for i in range(levels):
        e = list[i]
        electrons_per_level.append(e)

    
    def pen_jump(pen, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()

    def turtle_pen(shape="turtle", speed=10, size=3, colors=("blue", "green")):
        draw.shape(shape)
        draw.speed(speed)
        draw.pensize(size)
        draw.color(*colors)
        pen_jump(draw, 0, 0)
        draw.stamp()
        return draw
    def turtle_teardown(pen):
        pen.hideturtle()
    pen = turtle_pen()
    draw_atom(pen, first_level_radius, levels, electrons_per_level)
    turtle_teardown(pen)
    
    

def IonCompound(sx,sy,x,y):
    xtest = 0
    ytest = 0
    if x > 4:
        b1 = 8 - x
        xd = str(sx) + str(b1)+"-"
        xtest = -1
    elif x < 4:
        b1 = x
        xd = str(sx) + str(b1) + "+"
        xtest=1
    if b1==4 or b1==8 or b1==0:
        return 0
    if y > 4:
        b2 = 8 - y
        yd = str(sy) + str(b2) + "-"
        ytest = -1
    elif y < 4:
        b2 = y
        yd = str(sy) + str(b2) + "+"
        ytest = 1
    if b2 == 4 or b2 == 8 or b2==0:
        return 0
    if ytest==xtest:
        return 0

    if b1 == b2:
        x1 = sx+sy
    else:
        x1 = sx+str(b2)+sy+str(b1)
    return {
        "x" : xd,
        "y" : yd,
        "result" : x1
    }