# layer 0: Background object
# layer 1: foreground object

world = [[], []]

def add_object(o, depth = 0):
    if depth < 0 or depth >= len(world):
        raise IndexError('Invalid depth')
    world[depth].append(o)

def add_objects(ol, depth = 0):
    if depth < 0 or depth >= len(world):
        raise IndexError('Invalid depth')
    world[depth].extend(ol)

def update():
    for layer in world:
        for o in layer[:]:  # 복사본으로 순회하여 중간 삭제 안전화
            o.update()

def render():
    for layer in world:
        for o in layer[:]:  # 복사본으로 순회
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
