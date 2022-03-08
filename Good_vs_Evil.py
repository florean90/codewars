def goodVsEvil(good, evil):
    good_list = [int(i) for i in good.split()]
    evil_list = [int(i) for i in evil.split()]
    good_forces = [1, 2, 3, 3, 4, 10]
    evil_forces = [1, 2, 2, 2, 3, 5, 10]
    good_worth = sum(good_list[i]*good_forces[i] for i in range(len(good_list)))
    evil_worth = sum(evil_list[i]*evil_forces[i] for i in range(len(evil_list)))
    if good_worth > evil_worth:
        return "Battle Result: Good triumphs over Evil"
    elif good_worth < evil_worth:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"








print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))