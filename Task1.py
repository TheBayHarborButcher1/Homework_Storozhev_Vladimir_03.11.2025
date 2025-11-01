documents = [
    {'type': 'passport', 'number': '2287 876234', 'name': 'Василий Гулкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

def find_owner(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            doc_number = input('Введите номер документа: ')
            owner = find_owner(doc_number)
            if owner:
                print(f'Владелец документа: {owner}')
            else:
                print('Владелец документа: владелец не найден')
        elif command == 'q':
            break

if __name__ == "__main__":
    main()