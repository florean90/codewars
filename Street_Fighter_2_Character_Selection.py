def street_fighter_selection(fighters, initial_position, moves):
    result = []
    current_position = list(initial_position)
    for move in moves:
        if move == "right":
            current_position[1] = (current_position[1] + 1) % len(fighters[1])
        elif move == "left":
            current_position[1] = (current_position[1] - 1) % len(fighters[1])
        elif move == "up":
            if current_position[0] > 0:
                current_position[0] = (current_position[0] - 1)
        elif move == "down":
            if current_position[0] < len(fighters) - 1:
                current_position[0] = (current_position[0] + 1)
        result.append(fighters[current_position[0]][current_position[1]])
    return result


# def street_fighter_selection(fighters, initial_position, moves):
#     result = []
#     current_position = list(initial_position)
#     for move in moves:
#         if move == "right":
#             if current_position[1] < 5:
#                 current_position[1] += 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#             else:
#                 current_position[1] -= len(fighters[1]) - 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#         elif move == "left":
#             if current_position[1] > 0:
#                 current_position[1] -= 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#             else:
#                 current_position[1] += len(fighters[1]) - 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#         elif move == "up":
#             if current_position[0] > 0:
#                 current_position[0] -= 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#             else:
#                 result.append(fighters[current_position[0]][current_position[1]])
#         elif move == "down":
#             if current_position[0] < len(fighters) - 1:
#                 current_position[0] += 1
#                 result.append(fighters[current_position[0]][current_position[1]])
#             else:
#                 result.append(fighters[current_position[0]][current_position[1]])
#     return result




fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

initial_position = (0,0)
moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']


print(street_fighter_selection(fighters, initial_position, moves))
