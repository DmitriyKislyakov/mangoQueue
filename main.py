import collections
class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


you = Person('Dima', 'proger')
juli = Person('Juli', 'engeneer')
pasha = Person('Pasha', profession='taxi')
kirill = Person(name='Kirill', profession='businessman')
andrey = Person('Andrey', 'builder')
katyaP = Person('Katya', 'doctor')
misha = Person('Misha', 'seller')
nastya = Person('Nastya', 'businessman')
katya = Person('Katya', 'bank-manager')
alena = Person('Alena', 'visage')

myFriends = [juli, pasha, kirill]
pashaFriends = [kirill, andrey, katyaP]
kirillFriends = [pasha, misha, nastya]
juliFriends = [katya, alena]
visited = set()
graph = {you: myFriends, juli: juliFriends, pasha: pashaFriends, kirill: kirillFriends}

if __name__ == '__main__':
    print(you.__dict__)
    print(graph[juli])
