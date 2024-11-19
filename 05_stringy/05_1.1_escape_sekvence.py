print(len('ahoj'))
print(len("""Ahoj!"""))
print(len('a b'))
print(len( ' a b ' ))
print(len('\N{SNOWMAN}ové'))
print(len('a\nb'))
print(len('a\tb'))
print(len('"\'"'))
print(len("""
abc"""))
if True:
    print(len("""a
    b"""))
print(len('C:\new_dir'))
print(len(f'{print}'))      # print(len('<built-in function print>'))
