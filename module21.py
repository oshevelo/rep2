def calcnumb(a,do,c):
    if do in {"+","-","*","/","**","%","//"}:#FIXME: add checks for value error
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
    else: 
        print('wrong command')
def calcdate(a,do,c):
    if do == '+':
        return c + a
    elif do == '-':
        return c - a
    
