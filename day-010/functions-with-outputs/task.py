def format_name(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()

    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("reNan", "kinderMANN")

print(formated_string)


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)
