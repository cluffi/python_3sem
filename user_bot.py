def script(check, x, y):
    directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
    
    if check('gold', x, y):
        return 'take'

    queue = [(x, y, [])]
    visited = set()

    while queue:
        cx, cy, path = queue.pop(0)
        visited.add((cx, cy))

        for direction, (dx, dy) in directions.items():
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in visited or check('wall', nx, ny) or check('player', nx, ny):
                continue
            if check('gold', nx, ny):
                return path[0] if path else direction
            queue.append((nx, ny, path + [direction]))

    return 'pass'