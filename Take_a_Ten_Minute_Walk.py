def is_valid_walk(walk):
    return walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w") and len(walk) == 10







a = ['n','s','n','s','n','s','n','s','n','s']
print(is_valid_walk(a))