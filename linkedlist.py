'''
    Node class'ını kullanarak bir bağlı liste oluşturabiliriz.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None # Bağlamak istediğimiz bir sonra ki node değeridir.

'''
    Bağlı liste oluşturma classı
'''
class LinkedList():
    def __init__(self):
        self.header = None # Header noktasını belirliyoruz.

    # traversing işlemi yapmak için sırayla tüm verileri yazdırıyoruz.
    def printAllValuesOfNodes(self):
        temp = self.header
        while temp is not None:
            print(temp.value)
            temp = temp.nextNode

    # Yeni node'u başından ekleme fonksiyonu
    def AtBegining(self,value):
        newNode = Node(value)
        # Oluşturduğumuz yeni node değerinin pointerı eski header olmalıdır
        newNode.nextNode = self.header
        # Artık baştan yeni eleman eklediğimiz için header yeni node olmalıdır.
        self.header = newNode

# Bağlı listemizi oluştruduk.
listLinked = LinkedList()

# Headerımızı başa yerleştirdik.
listLinked.header = Node(1)
# Nodelarımızı oluşturduk
e2 = Node(2)
e3 = Node(3)

# Headerın nextNode'unu e2 ye bağladık
listLinked.header.nextNode = e2
#e2 nin next nodunu e3 e bağladık.
e2.nextNode = e3
# E3'ün sonu ise None olduğu için bir yere bağlama gereksinimi duymadık bu bizim için tailor oldu.

listLinked.AtBegining("oğuzhan")
listLinked.AtBegining("Sefa")
listLinked.printAllValuesOfNodes()

