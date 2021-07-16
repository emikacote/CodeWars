def snake_collision(field, moves):
    orientation, N, snake = ('R', 0, [[0, 0, 0], [0, 1, 2]])
    field = [['-' if field[i][j] == 'o' else field[i][j] for j in range(len(field[0]))] for i in range(len(field))]
    for move in moves.split():
        if move.isdigit():
            for i in range(int(move)):
                field, field_entry, head = get_field_entry(field, orientation, [snake[0][-1], snake[1][-1]])
                if field_entry is None:
                    return (snake[0][-1], snake[1][-1]), N+1
                N += 1
                [snake[i].append(head[i]) for i in range(2)]
                snake_new = move_snake(snake, field_entry)
                if snake_new is None: return (snake[0][-2], snake[1][-2]), N
                snake = snake_new
        else: orientation = move
    return (snake[0][-1], snake[1][-1]), N

def get_field_entry(field, orientation, head):
    ind, inc = (1, 1)
    if orientation == 'D' or orientation == 'U':
        ind = 0
    if orientation == 'L' or orientation == 'U':
        inc = -1
    head[ind] += inc
    print((head[0],head[1]))
    if head[0] <= 12 and head[0] >= 0 and head[1] <= 20 and head[1] >= 0:
       field_entry = field[head[0]][head[1]]
       field[head[0]][head[1]] = '-'
       return field, field_entry, head
    else: return (None,)*3

def move_snake(snake, field_entry):
    print(field_entry)
    if field_entry == '-':
        snake = [snake[i][1:] for i in range(2)]
    a = list(zip(snake[0], snake[1]))
    if len(a) != len(set(a)):
        return None
    return snake
