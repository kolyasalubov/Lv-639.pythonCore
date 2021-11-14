def bool_to_word(boolean):
    if bool(boolean) == 1:
        return "Yes"
    elif bool(boolean) == 0:
        return "No"