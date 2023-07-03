def check_straight_line(coordinates):
    # Helper function to calculate the slope between two points
    def slope(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')  

    # Get the first two points from the coordinates array
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Calculate the initial slope
    initial_slope = slope(x1, y1, x2, y2)

    # Check the remaining points
    for i in range(2, len(coordinates)):
        x_i, y_i = coordinates[i]
        if slope(x1, y1, x_i, y_i) != initial_slope:
            return False

    return True




# Example usage in the driver code 
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(check_straight_line(coordinates))  # Output: True
