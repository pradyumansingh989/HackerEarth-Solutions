for t in range(int(input())):
    green, purple = map(int, input().split())
    f_prob = []
    s_prob = []
    for n in range(int(input())):
        i, j = input().split()
        f_prob.append(int(i))
        s_prob.append(int(j))
    print((min(sum(f_prob), sum(s_prob)) * max(green, purple)) + (max(sum(f_prob), sum(s_prob)) * min(green, purple)))