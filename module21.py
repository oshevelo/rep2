def calc(a, do, c):
    if do in {"+","-","*","/","**","%","//"}:
        if do == '+':
            d = float(c) + float(a)
            return d
        elif do == '-':
            d = float(c) - float(a)
            return d
        elif do == '*':
            d = float(c) * float(a)
            return d
        elif do == '**':
            d = float(c) ** float(a)
            return d
        elif do == '/':
            d = float(c) / float(a)
            return d
        elif do == '%':
            d = float(c) % float(a)
            return d
        elif do == '//':
            d = float(c) // float(a)
            return d

