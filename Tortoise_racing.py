def race(v1, v2, g):
    if v1 > v2:
        return None
    difeerence = int(g * 3600 / (v2 - v1))
    return [difeerence // 3600, difeerence % 3600 // 60, difeerence % 60]


# def race(v1, v2, g):
#     if v1 > v2:
#         return None
#     diference = g / (v2 - v1) * 60 * 60
#     # print(diference)
#     minutes, seconds = divmod(diference, 60)
#     hours, minutes = divmod(minutes, 60)
#     return [int(hours), int(minutes), int(seconds)]





print(race(820, 850, 550))
print(race(480, 755, 66))