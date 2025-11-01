directories = {
    '1': ['2287 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_shelf(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None

def main():
    while True:
        command = input('Введите команду: ')
        if command == 's':
            doc_number = input('Введите номер документа: ')
            shelf = find_shelf(doc_number)
            if shelf:
                print(f'Документ хранится на полке: {shelf}')
            else:
                print('Документ не найден')
        elif command == 'q':
            break

if __name__ == "__main__":
    main()