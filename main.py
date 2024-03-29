from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value) 

class Name(Field):
   
    # реалізація класу
     def __init__(self, value):
        super().__init__(value)
	

class Phone(Field):
    # реалізація класу
    def __init__(self,value ):
        if re.fullmatch(r"\d{10}", value):
            super().__init__(value)
        else:
            raise ValueError('Невалідний телефон!')
	
    
          
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone(self, phone_num):  
        self.phones.append(Phone(phone_num)) 

    def remove_phone(self,phone_num):
        self.phones=[p for p in self.phones if str(p) != phone_num]

    def edit_phone(self, phone_num, phone_new):
        for p in self.phones:
            if str(p) == phone_num:
                self.phones.remove(p)
                self.phones.append(Phone(phone_new))
                print(f"Номер {self.name} змінено!")
           
    
    def find_phone(self, phone_num):
        for p in self.phones:
            if str(p)==phone_num:
                return f"Номер {self.name} - {phone_num} знайдено!"


    
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value]=record


    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        if name in self.data:
            self.data.pop(name)
            print("Запис видалено")
        else: 
            print("Запис не знайдено")
        

            


# Створення нової адресної книги
book = AddressBook( )

 # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

 # Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

 # Виведення всіх записів у книзі
for name, record in book.data.items():
     print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
 
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")