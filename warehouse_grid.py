class WarehouseGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Create empty grid
        self.grid = [["." for _ in range(width)] for _ in range(height)]
        
        # Define start and goal
        self.start = (0, 0)
        self.goal = (height-1, width-1)
        
        # Add obstacles
        self.obstacles = [(1,2), (2,2), (3,2), (3,3)]
        
        for x, y in self.obstacles:
            self.grid[x][y] = "#"

    def display_grid(self):
        for row in self.grid:
            print(" ".join(row))


if __name__ == "__main__":
    warehouse = WarehouseGrid(6,6)
    warehouse.display_grid()
