# Сортировка прямоугольников и кругов по площади II

# Ваша задача — вернуть новую последовательность измерений, отсортированных по возрастанию по площади.
# [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]   --> [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ]

def sort_by_area(seq):
    ret = []
    for el in seq:
        if type(el) == float or type(el) == int:
            ret.append([el, 3.1416 * (el**2)])
        elif type(el) == tuple:
            ret.append([el, el[0] * el[1]])
    return [el[0] for el in sorted(ret, key=lambda x: x[1])]

print(sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]))