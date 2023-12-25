from .flight_operations import add_flight, print_flights, search_flights_by_aircraft_type

def main():
    flights_list = []

    while True:
        print("Выберите действие:")
        print("1. Добавить рейс")
        print("2. Вывести список рейсов")
        print("3. Поиск рейсов по типу самолета")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            flight = add_flight()
            flights_list.append(flight)
            flights_list.sort(key=lambda x: x['название пункта назначения'])

        elif choice == '2':
            print_flights(flights_list)

        elif choice == '3':
            search_flights_by_aircraft_type(flights_list)

        elif choice == '4':
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == '__main__':
    main()

