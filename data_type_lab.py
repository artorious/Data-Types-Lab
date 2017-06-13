def data_type(user_input):
    """Takes one argument user_input
    """
    if isinstance(user_input, str):
        return len(user_input)
    elif user_input is None:
        return 'no value'
    elif isinstance(user_input, bool):
        return user_input
    elif isinstance(user_input, int):
        if user_input < 100:
            return "less than 100"
        elif user_input > 100:
            return "more than 100"
        else:
            return "equal to 100"
    elif isinstance(user_input, list):
        try:
            return user_input[2]
        except IndexError:
            return None
         
             
        
        
        