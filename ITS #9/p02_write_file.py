names = "Billy Bobby Sammy Willy Dilly Joe".split()

FILENAME = "write.txt"

with open(FILENAME, "w") as f:
    # for name in names:
    #     f.write(f"{name}\n")
    f.write("\n".join(names))
