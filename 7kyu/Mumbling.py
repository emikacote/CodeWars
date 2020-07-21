def accum(s):
    acum_st = []
    list(s)
    for i in range(len(s)):
        if i == 0:
            acum_st.insert(i, (s[i]).upper())
        elif i >= 1 and (s[i]).islower():
            acum_st.insert(i,(s[i]).upper()+(i)*s[i])
        else:
            acum_st.insert(i, (s[i]) + (i) * (s[i]).lower())
    return "-".join(acum_st)
