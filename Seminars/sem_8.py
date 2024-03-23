# 
def read_contacts(file_name):
    contacts = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    return contacts

def display_contacts(contacts):
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {', '.join(contact)}")

def search_contact_by_lastname(contacts, lastname):
    result = [contact for contact in contacts if lastname.lower() in contact[0].lower()]
    return result

def search_contact_by_phone(contacts, phone):
        result = [contact for contact in contacts if phone in contact[3]]
        return result
    
def add_contact(contacts):
    new_contact = input("Введите данные нового контакта (Фамилия, Имя, Описание, Номер телефона): ").split(',')
    contacts.append(new_contact)
    print("Контакт успешно добавлен.")


def delete_contact(contacts, index):
    if 0 < index <= len(contacts):
        del contacts[index - 1]
        print("Контакт успешно удален.")
    else:
        print("Неверный индекс контакта.")

def write_contacts(file_name, contacts):
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def copy_contact(source_file, destination_file, line_number):
    contacts = read_contacts(source_file)
    if 0 < line_number <= len(contacts):
        contact_to_copy = contacts[line_number - 1]
        with open(destination_file, 'a', encoding='utf-8') as file:
            file.write(','.join(contact_to_copy) + '\n')
        print(f"Контакт скопирован в файл {destination_file}.")
    else:
        print("Неверный номер строки.")

# Интерфейс справочника
file_name = 'contacts.txt'
contacts = read_contacts(file_name)

while True:
    print("\n1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Удалить запись")
    print("6. Сохранить контакты в файл")
    print("7. Скопировать контакт из одного файла в другой")
    print("8. Закончить работу")

    choice = input("Выберите действие: ")

    if choice == '1':
        print("\nСправочник контактов:")
        display_contacts(contacts)
    elif choice == '2':
        lastname = input("Введите фамилию для поиска: ")
        search_results = search_contact_by_lastname(contacts, lastname)
        print("\nРезультаты поиска:")
        display_contacts(search_results)
    elif choice == '3':
        phone = input("Введите номер телефона для поиска: ")
        search_results = search_contact_by_phone(contacts, phone)
        print("\nРезультаты поиска:")
        display_contacts(search_results)
    elif choice == '4':
        add_contact(contacts)
    elif choice == '5':
        index = int(input("Введите индекс контакта для удаления: "))
        delete_contact(contacts, index)
    elif choice == '6':
        write_contacts('new_contacts.txt', contacts)
        print("Контакты сохранены в файле 'new_contacts.txt'")
    elif choice == '7':
        line_number = int(input("Введите номер строки для копирования: "))
        copy_contact(file_name, 'copied_contacts.txt', line_number)
    elif choice == '8':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
