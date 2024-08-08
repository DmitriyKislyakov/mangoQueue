from collections import deque
class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


#persons
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

#persons friends
myFriends = [juli, pasha, kirill]
pashaFriends = [kirill, andrey, katyaP]
kirillFriends = [pasha, misha, nastya]
juliFriends = [katya, alena]

#friends graphs
graph = {you: myFriends, juli: juliFriends, pasha: pashaFriends, kirill: kirillFriends, andrey: [], katyaP: [], misha: [], nastya: [], katya: [], alena:[alena]}

#search seller function:
def searchSeller():
    searched = set()
    sellerDeque = deque()
    sellerDeque += graph[you]
    while sellerDeque:
        personDeque = sellerDeque.popleft()
        print(personDeque.name, personDeque.profession)
        if not personDeque in searched:
            if personDeque.profession == 'seller':
                return print(f'{personDeque.name} is seller!')
            else:
                sellerDeque += graph[personDeque]
            searched.add(personDeque)
    return print('Nobody is seller')




if __name__ == '__main__':
    searchSeller()
