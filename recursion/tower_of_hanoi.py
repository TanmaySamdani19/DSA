def solve(s, d, h, n):
    if n == 1:
        print(f"Move disk {n} from {s} to {d}")
        return
    solve(s, h, d, n - 1)
    print(f"Move disk {n} from {s} to {d}" )
    solve(h, d, s, n -1)
    return

print(solve("A", "C", "B", 3))