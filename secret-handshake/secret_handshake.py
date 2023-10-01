def commands(binary_str: str):
    binary_list: list = [int(item) for item in binary_str]
    commands: list = ["wink", "double blink", "close your eyes", "jump"]
    binary_list.reverse()
    commands_list: list = []
    for index, item in enumerate(binary_list):
        if index == 4:
            break
        if item == 1:
            commands_list.append(commands[index])

    if binary_list[4] == 1:
        commands_list.reverse()
    return commands_list
