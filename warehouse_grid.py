from astar import astar

class WarehouseGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [["." for _ in range(width)] for _ in range(height)]

        self.start = (0, 0)
        self.goal = (height - 1, width - 1)

        self.obstacles = []

        for x, y in self.obstacles:
            self.grid[x][y] = "#"

    def display_grid(self):
        for row in self.grid:
            print(" ".join(row))


if __name__ == "__main__":
    warehouse = WarehouseGrid(6, 6)
    warehouse.display_grid()

    current_position = warehouse.start
    goal = warehouse.goal

    # traffic simulation
    traffic = {
        (0, 3): 5,
        (1, 5): 3
    }

    print("\nStart:", current_position)
    print("Goal:", goal)

    step = 0

    while current_position != goal:
        print(f"\nStep {step}: Robot at {current_position}")
        # simulate changing traffic
        if step == 1:
            print("Blocking column 1")
            for i in range(6):
                warehouse.grid[i][1] = "#"

        path = astar(warehouse.grid, current_position, goal, traffic)

        if not path:
            print("No path found!")
            break

        print("New Path:", path)

        # move one step
        current_position = path[0]

        step += 1

    print("\nReached Goal!")
