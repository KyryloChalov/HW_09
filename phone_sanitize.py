def format_phone_number(func):
    def inner(phone):
        new_phone = func(phone)
        if len(new_phone) == 9:
            new_phone = '+380' + new_phone
        elif len(new_phone) == 10:
            new_phone = '+38' + new_phone
        elif len(new_phone) == 12:
            new_phone = '+' + new_phone
        else:
            new_phone = f"{phone} - incorrect phone number"
        return new_phone
    return inner           


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone
