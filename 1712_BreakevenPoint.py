A, B, C = map(int, input().split())    # A:고정비용, B:가변비용, C:제품가격

if B >= C:
    print(-1)
else:
    print(f'{A // (C - B) + 1}')
