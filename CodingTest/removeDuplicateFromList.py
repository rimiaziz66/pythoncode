def remove_duplicate(ls):

    new_ls = []

    for l in ls:
        if l in new_ls:
            continue;
        else:
            new_ls.append(l)
    return new_ls


a= remove_duplicate([2,3,4,4])
print(a)


