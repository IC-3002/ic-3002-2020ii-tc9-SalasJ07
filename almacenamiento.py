def maximizar(As, D):
    z = 1
    As.sort(key = lambda x: x[1])
    res = 0
    M = []
    for item in As:
        if res + item[1] > D:
            break
        else:            
            res += item[1]
            M.append(item)
    return M
    

