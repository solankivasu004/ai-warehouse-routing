import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal, traffic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        x, y = current

        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for neighbor in neighbors:
            nx, ny = neighbor

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):

                if grid[nx][ny] == "#":
                    continue

                traffic_cost = traffic.get(neighbor, 0)

                tentative_g = g_score[current] + 1 + traffic_cost

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g

                    f = tentative_g + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None
