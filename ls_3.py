# count = 9
# if count < 10:
#     count += 1
# else:
#     pass
# print(count)


# anim = 'bird'
# if anim == 'cat':
#     print('Meo')
# elif anim == 'dog':
#     print('Wof')
# else:
#     print("I don't know this animal.")


# count = 0
# rest = True if count > 1 else 'bye'
# print(rest)


# grin = 356
# if grin > 1000:
#     grin = grin * 0.9
# elif grin > 500:
#     grin = grin * 0.95
# elif grin > 100:
#     grin = grin * 0.97
# else:
#     pass
# print(grin)


# result = 'hello'
# rest = None if result == None else result
# print(rest)


firs_v = 60
second_v = 5
button = '/'
if firs_v is None or second_v is None:
    print("Пишите только число")
else:
    if button == '+':
        firs_v += second_v
    elif button == '-':
        firs_v -= second_v
    elif button == '*':
        firs_v *= second_v
    elif button == '/':
        if second_v == 0:
            print("Повтори")
        else:
            firs_v /= second_v
    else:
        pass
    print("Ваш ответ", firs_v)
