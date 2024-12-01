# age: int  # specify the type
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    # "->" specifies the data type return statement
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass.")
else:
    print("Pay fine.")