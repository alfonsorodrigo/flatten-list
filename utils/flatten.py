def flatten_list(input_list: list, output_list: list = []) -> list:
    for item in input_list:
        output_list.append(item) if type(item) is not list else flatten_list(
            item, output_list
        )
    return output_list
