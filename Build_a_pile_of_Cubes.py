def find_nb(m):
    volume = 0
    levels = 0
    while volume < m:
        levels +=1
        volume += levels**3
        if volume == m:
            return levels
    return -1
















print(find_nb(1071225))
print(find_nb(91716553919377))