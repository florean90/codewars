def in_array(array1, array2):
    return sorted(list({i for i in array1 for j in array2 if i in j}))




print(in_array(["live", "strong", "arp"],["lively", "alive", "harp", "sharp", "armstrong"]))