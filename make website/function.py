
# #f(x) = x^2 + 2x + 6
# def simp_c(x):
#     total = x**2 + 2*x + 6
#     return total
# #print(simp_c(3))
# #add function
# def add(x,y):
#     total = x+y
#     return total
# print(add(2,3))
# print('again')
# print(add(3,4))

# #slugify
# data = input('enter key: ')
# def slugify(text):
#     slug = text.strip().lower().replace(' ', '-')
#     while '--' in slug:
#         slug = slug.replace('---', '-')
#     return slug

# out = slugify(data)
# print(out)


#TRIANGLE, SQUARE, RECTANGLE

def tgle(base, height):
    area = 0.5 * base * height
    return area

def sqare(length):
    area = length * length
    return area

def rect(length, width):
    area = length * width
    return area

# out = sqare(5), tgle(3, 5), rect(5, 7)
# print(out)
# #out = sqare(5)
# #out = tgle(5, 3)

#UNLIMITED ARGUMENT PASSING

# def single(a, b):
#     total = a+b
#     return total

# print(single(2, 3))

# def unliimted_arg(*args):
#     total = 0
#     for numbers in args:
#         #total+= numbers
#         #total = total + numbers
#     return total
# data = unliimted_arg(1,2,3,4,5,6,7)
# print(data)






