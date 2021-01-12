# X
types_of_people = 2
x = f"est' {types_of_people} tipa ludei"

# Y
binary = "Python"
do_not = "net"
y = f"te, kto ponimaet {binary}, i te, kto - {do_not}"

# print
print(x)
print(y)

print(f"ya skazal: {x}")
print(f"A esche ya skazal: '{y}'")

hilarious = False
joke_evuluation = "Razve eto ne smeshno?! {}"
print(joke_evuluation.format(hilarious))
#         ^             ^          ^
#эта часть - текст/это формат/это значение

w="right."
e="..left"
print(w + e)