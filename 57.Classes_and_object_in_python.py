class Person:
    name = 'Bilal'
    occupation = 'Devoloper'
    newworth = 30000

    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = Person()
print(a.name)
print(a.info())

b = Person()
b.name = 'danyal'
print(b.name)
print(b.info())