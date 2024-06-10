def find_internal_nodes_num(tree):
    found = []
    for x in tree:
        if x not in found and x != -1:
            found.append(x)
    return len(found)
