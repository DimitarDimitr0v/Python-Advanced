def math_operations(*args, **kwargs):
    for i in range(0, len(args), 4):

        a = args[i] if i < len(args) else 0
        s = args[i + 1] if i + 1 < len(args) else 0
        d = args[i + 2] if i + 2 < len(args) else 1
        m = args[i + 3] if i + 3 < len(args) else 1

        if d == 0:
            d = 1

        kwargs["a"] += a
        kwargs["s"] -= s
        kwargs["d"] /= d
        kwargs["m"] *= m

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{item[0]}: {item[1]:.1f}" for item in sorted_kwargs)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))
