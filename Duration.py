n = int(input())
for i in range(n):
    sh,sm,eh,em = input().split()
    sh = int(sh)
    sm = int(sm)
    eh = int(eh)
    em = int(em)
    s=(sh*60)+sm
    e=(eh*60)+em
    ans=e-s
    wh=ans//60
    wm=ans%60
    print(wh,wm)