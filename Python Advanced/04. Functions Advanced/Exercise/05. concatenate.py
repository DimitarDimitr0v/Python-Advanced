def concatenate(*args, **kwargs):
    args = "".join(args)

    for k, v in kwargs.items():
        if k in args:
            args = args.replace(k, v)

    return args


print(concatenate("Soft", "UNI", "Is", "Grate", "!",

                  UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",

C="P", s="", java='Java'))