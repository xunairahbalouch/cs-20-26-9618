class Animal:
    """Task 2.1: Animal class"""
    def __init__(self, animal_id, name, species, age):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.next = None
    
    def __str__(self):
        return f"ID: {self.animal_id}, Name: {self.name}, Species: {self.species}, Age: {self.age}"


class AnimalShelter:
    """Task 2.2: Animal shelter queue using linked list"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def IsEmpty(self):
        """Task 2.1: Check if shelter is empty"""
        return self.head is None
    
    def Enqueue(self, animal):
        """Task 2.2: Add animal to the shelter (end of queue)"""
        animal.next = None
        
        if self.tail is None:
            self.head = animal
            self.tail = animal
        else:
            self.tail.next = animal
            self.tail = animal
        
        self.count += 1
        print(f"Enqueued: {animal.name}")
    
    def Dequeue(self):
        """Task 2.2: Remove and return animal from front of queue"""
        if self.IsEmpty():
            print("Shelter is empty")
            return None
        
        animal = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
        
        animal.next = None
        self.count -= 1
        print(f"Dequeued: {animal.name}")
        return animal
    
    def Peek(self):
        """Task 2.2: View next animal without removing"""
        if self.IsEmpty():
            return None
        return self.head
    
    def DisplayAll(self):
        """Task 2.2: Display all animals in the shelter"""
        if self.IsEmpty():
            print("Shelter is empty")
            return
        
        print("Animals in shelter (front to back):")
        current = self.head
        while current:
            print(f"  {current}")
            current = current.next
        
        print(f"Total animals: {self.count}")
    
    def DisplayBySpecies(self, species):
        """Task 2.3: Display animals of a specific species"""
        current = self.head
        found = False
        
        while current:
            if current.species == species:
                print(current)
                found = True
            current = current.next
        
        if not found:
            print(f"No {species} found in shelter")
    
    def CountBySpecies(self, species):
        """Task 2.3: Count animals by species"""
        count = 0
        current = self.head
        
        while current:
            if current.species == species:
                count += 1
            current = current.next
        
        print(f"Total {species}: {count}")
        return count
    
    def SearchByName(self, name):
        """Task 2.4: Search for animal by name"""
        current = self.head
        search_lower = name.lower()
        
        while current:
            if current.name.lower() == search_lower:
                return current
            current = current.next
        
        return None


def BubbleSortAnimals(shelter, sort_by="name"):
    """Task 2.4: Sort animals using bubble sort"""
    animals = []
    current = shelter.head
    
    while current:
        animals.append(current)
        current = current.next
    
    n = len(animals)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            should_swap = False
            
            if sort_by == "name":
                if animals[j].name > animals[j + 1].name:
                    should_swap = True
            elif sort_by == "age":
                if animals[j].age > animals[j + 1].age:
                    should_swap = True
            elif sort_by == "species":
                if animals[j].species > animals[j + 1].species:
                    should_swap = True
            
            if should_swap:
                animals[j], animals[j + 1] = animals[j + 1], animals[j]
    
    shelter.head = None
    shelter.tail = None
    shelter.count = 0
    
    for animal in animals:
        shelter.Enqueue(animal)


def SelectionSortAnimals(shelter, sort_by="name"):
    """Task 2.4: Sort animals using selection sort"""
    animals = []
    current = shelter.head
    
    while current:
        animals.append(current)
        current = current.next
    
    n = len(animals)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sort_by == "name":
                if animals[j].name < animals[min_idx].name:
                    min_idx = j
            elif sort_by == "age":
                if animals[j].age < animals[min_idx].age:
                    min_idx = j
        
        animals[i], animals[min_idx] = animals[min_idx], animals[i]
    
    shelter.head = None
    shelter.tail = None
    shelter.count = 0
    
    for animal in animals:
        shelter.Enqueue(animal)


if __name__ == "__main__":
    shelter = AnimalShelter()
    
    print("=" * 80)
    print("Task 2.1 & 2.2: Animal Shelter Queue")
    print("=" * 80)
    
    animal1 = Animal("A001", "Max", "Dog", 3)
    animal2 = Animal("A002", "Whiskers", "Cat", 2)
    animal3 = Animal("A003", "Buddy", "Dog", 5)
    animal4 = Animal("A004", "Luna", "Cat", 1)
    
    shelter.Enqueue(animal1)
    shelter.Enqueue(animal2)
    shelter.Enqueue(animal3)
    shelter.Enqueue(animal4)
    
    print("\n" + "=" * 80)
    print("Display all animals")
    print("=" * 80)
    shelter.DisplayAll()
    
    print("\n" + "=" * 80)
    print("Task 2.3: Display by species")
    print("=" * 80)
    shelter.DisplayBySpecies("Dog")
    shelter.CountBySpecies("Dog")
    
    print("\n" + "=" * 80)
    print("Task 2.4: Search and Sort")
    print("=" * 80)
    found = shelter.SearchByName("Max")
    if found:
        print(f"Found: {found}")
    
    print("\nSorted by name:")
    SelectionSortAnimals(shelter, "name")
    shelter.DisplayAll()
