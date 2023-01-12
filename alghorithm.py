
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