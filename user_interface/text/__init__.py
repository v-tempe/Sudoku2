def get_raw_text_from_stdin(prompt: str = "") -> str:
    raw_text = input(prompt)
    return raw_text


def preprocess_text_user_response(raw_text: str):
    return raw_text.strip()


def process_text_user_response(user_raw_text: str) -> dict[str: str]:
    import constants

    user_response = preprocess_text_user_response(user_raw_text).split()
    result: dict[str: str] = dict()
    no_action: dict = dict()
    if not user_response:
        return no_action

    action = user_response.pop(0)
    incorrect_action: dict = {"incorrect_action": action}

    if action == constants.actions.commands.CHOOSE:
        if len(user_response) < 2:
            return incorrect_action
        result["action"] = action

        coor_x = user_response.pop(0)
        if not coor_x.isdigit():
            return incorrect_action
        result["x"] = coor_x

        coor_y = user_response.pop(0)
        if not coor_y.isdigit():
            return incorrect_action
        result["y"] = coor_y

    elif action == constants.actions.commands.SET_VALUE:
        if len(user_response) < 1:
            return incorrect_action
        result["action"] = action
        cell_value = user_response.pop(0)
        if not cell_value.isdigit():
            return incorrect_action
        result["value"] = cell_value

    elif action == constants.actions.commands.EXIT:
        result["action"] = action

    else:
        return incorrect_action
    return result
