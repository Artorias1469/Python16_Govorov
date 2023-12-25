def create_greeting(template):
    def inner_function(last_name, first_name):
        formatted_template = template.replace("%F%", last_name).replace("%N%", first_name)
        return formatted_template

    return inner_function

if __name__ == "__main__":
    greet_template = "Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций."
    greet_function = create_greeting(greet_template)

    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")

    result = greet_function(last_name, first_name)
    print(result)