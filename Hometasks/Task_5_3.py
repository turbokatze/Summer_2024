n = int(input())
f0, f1, count = 0, 1, 1
fn = f1

while count <= n:
    print(fn, end=" ")
    count += 1
    f0, f1 = f1, fn
    fn = f0 + f1
print()