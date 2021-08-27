n = int(input())
a = list(map(int, input().split()))
a_new = sorted(a, reverse=True)


alice = []
bob = []
for i in range(n):
    # Aliceが取るカード
    if (i+1) % 2 == 1:
        alice.append(a_new[i])
    # Bobが取るカード
    else:
        bob.append(a_new[i])

print(sum(alice) - sum(bob))
