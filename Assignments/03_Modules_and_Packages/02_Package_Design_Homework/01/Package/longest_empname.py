def longest_emp_name(x):
    x = x.split()
    l_name_emp = x[0]
    for i in x:
        if len(i)>len(l_name_emp):
            l_name_emp = i
    return l_name_emp