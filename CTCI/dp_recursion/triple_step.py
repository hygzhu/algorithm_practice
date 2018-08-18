"""
Given a staircase with n steps, count how many ways you can go up the stairs in 1,2 or 3 steps at a time
"""

def triple_step_recursive(n):

    #base cases
    if n == 0:
        return 0
    elif n== 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return triple_step_recursive(n-1) + triple_step_recursive(n-2) + triple_step_recursive(n-3)

def triple_step(n):
    num = [0]*(n+1)
    num[0] = 0
    num[1] = 1
    num[2] = 2
    num[3] = 4
    for i in range(4, n+1):
        num[i] = num[i-1] + num[i-2] + num[i-3]
    return num[n]


print(triple_step_recursive(10))
print(triple_step(10))