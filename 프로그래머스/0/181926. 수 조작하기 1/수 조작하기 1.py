def solution(n, control):
    control_dict = {"w":1, "s":-1, "d":10, "a":-10}
    for i in control:
        n += control_dict[i]
    return n