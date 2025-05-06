N = int(input())

if N == 1:
    print(1)
else:
    layer=1
    while True:
        last_layer = 3 * layer * (layer+1) + 1
        if N <= last_layer:
            print(layer+1)
            break
        else:
            layer+=1