# A function that call themself, need 2 cases to work well a return case and a recursion case
def regressive(i):
    print(i)
    if i <= 0:
        return
    else:
        regressive(i-1)

regressive(5)