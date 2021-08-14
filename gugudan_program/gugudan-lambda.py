# condition (전제)
# given integer x, y
# x, y are in range 1..9

# function (lambda)
# z = f(x, y) = x * y
numbers = range(1,10)
z = lambda x, y : x * y # data, value
print(z)
for x in numbers:
    for y in numbers:
        print(f'{x} * {y} = {z(x, y)}')
