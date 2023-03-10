def get_char_count(string, pos):
    # (alpha: string.count(alpha) for alpha in string) :- This will give you count of each character in a string

    # sort the dict in descending order and returns a list of tuples
    count_of_each_chars = sorted({alpha: string.count(alpha) for alpha in string}.items(), key=lambda item: item[1],
                                 reverse=True)
    try:
        print(
            f"Position {pos} has Character '{count_of_each_chars[pos - 1][0]}' with count '{count_of_each_chars[pos - 1][1]}'")
    except:
        print("Invalid Position or Position Out of range")


def main():
    string = "".join(input("Enter String : ").split()).strip()
    is_pos_int = False
    pos = None
    # check for position is a number or not
    while not is_pos_int:
        pos = input("Enter position : ")
        is_pos_int = pos.isnumeric()
        if is_pos_int:
            pos = int(pos)

    get_char_count(string, pos)


if __name__ == '__main__':
    main()


# i/p = str = "Mississippi"
