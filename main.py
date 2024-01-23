class LinkedList:
    def __init__(self):
        self.head = None

    def vloz(self, prvok):
        if self.head is None:
            self.head = prvok
        else:
            aktualny = self.head
            while aktualny.next is not None:
                aktualny = aktualny.next
            aktualny.next = prvok


    def vypis(self):
        aktualny = self.head
        print(aktualny.data)
        while aktualny.next is not None:
            aktualny = aktualny.next
            print(aktualny.data)

    def vloz_na_zaciatok(self, prvok):
        if self.head is None:

            self.head = prvok
        else:
            predtym_prvy = self.head
            self.head = prvok
            prvok.next = predtym_prvy


class Prvok:
    def __init__(self, data):
        self.data = data
        self.next = None

mojLinked = LinkedList()
prvok1 = Prvok("Milan")
mojLinked.vloz_na_zaciatok(prvok1)
prvok2 = Prvok("Jozo")
mojLinked.vloz_na_zaciatok(prvok2)
prvok3 = Prvok("Fero")
mojLinked.vloz_na_zaciatok(prvok3)
mojLinked.vypis()
print("test")
