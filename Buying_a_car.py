def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    savedMoney = 0
    months = 0
    while startPriceOld + savedMoney < startPriceNew:
        months += 1
        if months % 2 == 0:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld / 100 * percentLossByMonth
        startPriceNew -= startPriceNew / 100 * percentLossByMonth
        savedMoney += savingperMonth
    return [months, int(round(startPriceOld + savedMoney - startPriceNew))]







print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 8000, 1000, 1.5))
print(nbMonths(7500, 32000, 300, 1.55))