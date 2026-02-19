import os
from src.utils import get_transactions
from src.file_readers import read_csv, read_excel
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.generators import filter_by_currency
from src.widget import mask_account_card, get_date


def main() -> None:
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    if choice == "1":
        file_path = os.path.join("data", "operations.json")
        transactions = get_transactions(file_path)
        print(f"Программа: Для обработки выбран JSON-файл {file_path}.")
    elif choice == "2":
        file_path = os.path.join("data", "transactions.csv")
        transactions = read_csv(file_path)
        print(f"Программа: Для обработки выбран CSV-файл {file_path}.")
    elif choice == "3":
        file_path = os.path.join("data", "transactions_excel.xlsx")
        transactions = read_excel(file_path)
        print(f"Программа: Для обработки выбран XLSX-файл {file_path}.")
    else:
        print("Программа: Некорректный выбор.")
        return

    if not transactions:
        print("Программа: Данные не загружены или файл пуст.")
        return

    # Status filtering loop
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").strip().upper()
        
        if status_input in valid_statuses:
            transactions = filter_by_state(transactions, status_input)
            print(f"Программа: Операции отфильтрованы по статусу \"{status_input}\"")
            break
        else:
            print(f"Программа: Статус операции \"{status_input}\" недоступен.")

    # Sorting
    sort_choice = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Программа: Отсортировать по возрастанию или по убыванию? \nПользователь: ").strip().lower()
        reverse = "убыванию" in order_choice
        transactions = sort_by_date(transactions, reverse=reverse)

    # Currency filtering
    rub_choice = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if rub_choice == "да":
        transactions = [tx for tx in filter_by_currency(transactions, "RUB")]

    # Keyword searching
    search_choice = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if search_choice == "да":
        keyword = input("Программа: Введите ключевое слово:\nПользователь: ").strip()
        transactions = process_bank_search(transactions, keyword)

    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(transactions)}\n")
        for tx in transactions:
            raw_date = tx.get("date", "")
            formatted_date = get_date(raw_date) if raw_date else "Неизвестно"
            description = tx.get("description", "Без описания")
            
            from_info = tx.get("from", "")
            masked_from = mask_account_card(from_info) if from_info else ""
            
            to_info = tx.get("to", "")
            masked_to = mask_account_card(to_info) if to_info else ""
            
            amount = tx.get("operationAmount", {}).get("amount", "0")
            currency_info = tx.get("operationAmount", {}).get("currency", {})
            currency_name = currency_info.get("name", "RUB")

            print(f"{formatted_date} {description}")
            if masked_from:
                print(f"{masked_from} -> {masked_to}")
            elif masked_to:
                print(f"{masked_to}")
            print(f"Сумма: {amount} {currency_name}\n")


if __name__ == "__main__":
    main()
