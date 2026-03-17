class Robot:
    def __init__(self, start_position):
        self.position = start_position

    def move(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position


def get_neighbors(position, grid):
    x, y = position
    
    # Possible moves (up, down, left, right)
    moves = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]
    
    valid_moves = []
    
    for nx, ny in moves:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != "#":  # not obstacle
                valid_moves.append((nx, ny))
    
    return valid_moves


if __name__ == "__main__":
    grid = [
        [".", ".", "."],
        [".", "#", "."],
        [".", ".", "."]
    ]

    robot = Robot((0, 0))
    
    print("Robot position:", robot.get_position())
    
    neighbors = get_neighbors(robot.get_position(), grid)
    print("Possible moves:", neighbors)
