def ConstantApproximator(terms):
    qtty = 0
    sum_n_minus_two_fact = 0
    n_fact = 1
    for n in range(1,terms+1):
        n_minus_one_fact = n_fact
        n_fact *= n
        qtty += sum_n_minus_two_fact/n_fact
        sum_n_minus_two_fact += n_minus_one_fact
    return qtty