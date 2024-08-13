def robotWalk(x):
    x_coord = 0
    y_coord = 0
    direction = 'up'  # Starting direction
    final_line = [[0, 0], [0, 0], 'none']  # Specifies pos and direction
    
    for i in range(len(x)):
        if direction == 'up':
            prev = [x_coord, y_coord]
            y_coord += x[i]
            curr = [x_coord, y_coord]
            final_line = [prev, curr, direction]
            direction = 'right'
        elif direction == 'right':
            prev = [x_coord, y_coord]
            x_coord += x[i]
            curr = [x_coord, y_coord]
            final_line = [prev, curr, direction]
            direction = 'down'
        elif direction == 'down':
            prev = [x_coord, y_coord]
            y_coord -= x[i]
            curr = [x_coord, y_coord]
            final_line = [prev, curr, direction]
            direction = 'left'
        elif direction == 'left':
            prev = [x_coord, y_coord]
            x_coord -= x[i]
            curr = [x_coord, y_coord]
            final_line = [prev, curr, direction]
            direction = 'up'

    '''
    Go back through and compare each line against final line
        checking for intersections
    '''
    x_coord = 0
    y_coord = 0
    direction = 'up'  # Starting direction
    check_line = [[0, 0], [0, 0], 'none']  # Specifies pos and direction
    
    for i in range(len(x)):
        if direction == 'up':
            prev = [x_coord, y_coord]
            y_coord += x[i]
            curr = [x_coord, y_coord]
            check_line = [prev, curr, direction]
            direction = 'right'
        elif direction == 'right':
            prev = [x_coord, y_coord]
            x_coord += x[i]
            curr = [x_coord, y_coord]
            check_line = [prev, curr, direction]
            direction = 'down'
        elif direction == 'down':
            prev = [x_coord, y_coord]
            y_coord -= x[i]
            curr = [x_coord, y_coord]
            check_line = [prev, curr, direction]
            direction = 'left'
        elif direction == 'left':
            prev = [x_coord, y_coord]
            x_coord -= x[i]
            curr = [x_coord, y_coord]
            check_line = [prev, curr, direction]
            direction = 'up'
            
        if len(x) > 3:
            # Check for intersecting lines
            if ((final_line[2] == 'up' or final_line[2] == 'down') and
                (check_line[2] == 'left' or check_line[2] == 'right')):
                # final_line is vertical
                # check_line is horizontal
                
                #big and small y values of vertical line
                small_y = min(final_line[0][1], final_line[1][1])
                big_y = max(final_line[0][1], final_line[1][1])
                
                # if y of horizontal line is between the lower and higher y values of the vertical line
                if check_line[0][1] >= small_y and check_line[0][1] <= big_y:
                    small_x = min(check_line[0][0], check_line[1][0])
                    big_x = max(check_line[0][0], check_line[1][0])
                    
                    # if x of vertical line is between the lower and higher x values of the horizontal line
                    if final_line[0][0] >= small_x and final_line[0][0] <= big_x:
                        return [final_line[0][0], check_line[0][1]]
                        
                    
            if ((final_line[2] == 'left' or final_line[2] == 'right') and
                (check_line[2] == 'up' or check_line[2] == 'down')):
                # final_line is horizontal
                # check_line is vertical
                
                small_y = min(check_line[0][1], check_line[1][1])
                big_y = max(check_line[0][1], check_line[1][1])
                
                # if y of horizontal line is between the lower and higher y values of the vertical line
                if final_line[0][1] >= small_y and final_line[0][1] <= big_y:
                    small_x = min(final_line[0][0], final_line[1][0])
                    big_x = max(final_line[0][0], final_line[1][0])
                    
                    # if x of vertical line is between the lower and higher x values of the horizontal line
                    if check_line[0][0] >= small_x and check_line[0][0] <= big_x:
                        return [check_line[0][0], final_line[0][1]]
        
    return final_line[1]

print(robotWalk([1, 2, 4, 1, 5]))  # Correct output: [1, 1]
print(robotWalk([1, 2, 4]))  # Correct output: [2, -3]