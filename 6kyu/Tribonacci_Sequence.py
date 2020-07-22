def tribonacci(signature, n):
    tri_list = signature
    tri_list.append(sum(signature))
    for i in range(4, n):
            tri_list.append(sum(tri_list[-3::1]))
            i += 1
    return tri_list[:n]
