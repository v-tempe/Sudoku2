import constants.actions


def main():
    import user_interface
    from sudoku import Sudoku

    sudoku = Sudoku()

    running = True
    while running:
        actions: list[dict[str: str]] = list()
        raw_user_response = user_interface.text.get_raw_text_from_stdin(constants.actions.INPUT_PROMPT)
        next_action: dict[str: str] = user_interface.text.process_text_user_response(raw_user_response)
        actions.append(next_action)
        print(actions)

        # stub
        if actions[0] and actions[0].get("action", False) == "exit":
            running = False


if __name__ == "__main__":
    main()
