from phone_sanitize import sanitize_phone_number

phonebook = {}


def user_error(func):

    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params.\nFormat: '<command> <name> <phone>'\nUse 'help' for information"
        except KeyError:
            return f"Unknown name {args[0]}. Try another or use help."
        # except UnboundLocalError:
        #     return f"Unknown name {args[0]}. Try another or use help."
    return inner


@user_error
def add_record(*args):
    
    name = args[0]
    phone = sanitize_phone_number(args[1])
    phonebook[name] = phone
    result = f"Add record:  {name = }, {phone = }"
    return result


@user_error
def change_record(*args):

    name = args[0]
    phone = sanitize_phone_number(args[1])
    rec = phonebook[name]
    if rec:
        phonebook[name] = phone
        return f"Change record:  {name = }, new{phone = }"


@user_error
def delete_record(*args):

    name = args[0]
    phone = sanitize_phone_number(args[1])
    rec = phonebook[name]
    if rec:
        phonebook.pop(name)
        return f"Record has been deleted:  {name = }, {phone = }"


@user_error
def find_phone(*args):

    for name, phone in phonebook.items():
        if args[0] == name:
            return f"{name} has a phone number {phone}"
    return "no such name"

@user_error
def find_name(*args):

    for name, phone in phonebook.items():
        if args[0] == phone:
            return f"{name} has a phone number {phone}"
    return "no such phone number"


def show_all(*args):
    temp_list = ["\tName\t\tPhone"]
    i = 0
    for name, phone in phonebook.items():
        i += 1
        temp_list.append(f"{i:>{3}}. {name:<{15}}{phone:<15}")
    result = "\n".join(temp_list)
    if i == 0:
        result = "\tNothing to output"
    return result


def help_page(*args):
    
    help_list = ["\tPhoneBook\tversion 1.2.3"]
    help_list.append('add record <name> <phone>     - add a new name with a phone number')
    help_list.append('change record <name> <phone>  - change the phone number for an existing record')
    help_list.append('delete record <name> <phone>  - delete an existing record')    
    help_list.append('phone <name>                  - search phone number by name')
    help_list.append('name <phone>                  - search name by phone number')
    help_list.append('show all                      - show all records')
    help_list.append('hello                         - "hello-string"')
    help_list.append('exit                          - exit from PhoneBook')
    help_list.append('help                          - this page')
    
    return "\n".join(help_list)


def say_hello(*args):
    return "How can I help you?"


def say_goodbay(*args):
    print("Good bye!")
    exit(0)

def unknown(*args):
    return "Unknown command. Try again. "


COMMANDS = {"add record": add_record, "add": add_record,
            "change record": change_record, "change": change_record,
            "delete record": delete_record, "delete": delete_record, "del": delete_record,
            "help": help_page,
            "hello": say_hello, "hi": say_hello,
            "phone": find_phone,
            "name": find_name,
            "show all": show_all, "show": show_all,
            "good by": say_goodbay, "by": say_goodbay, "close": say_goodbay, "exit": say_goodbay
            }


def parser(text: str):
    for kw, func in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input(">>>").strip().lower()
        func, data = parser(user_input)
        print(func(*data))


if __name__ == '__main__':
    main()