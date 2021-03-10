def check_board_rows_and_cols(board: list) -> bool:
    for indx in range(len(board)):
        unique_row_data = set()
        unique_col_data = set()
        # Check if data in row is unique
        for item in board[indx]:
            if item.isnumeric():
                if int(item) in unique_row_data:
                    return False
                else:
                    unique_row_data.add(int(item))
        # Check if data in column is unique
        for item in range(len(board)):
            tmp_data = board[item][indx]
            if tmp_data.isnumeric():
                if int(tmp_data) in unique_col_data:
                    return False
                else:
                    unique_col_data.add(int(tmp_data))
    return True


def check_board_color(board: list) -> bool:
    """
    Check if data in color cells is unique.
    """
    for color_row_indx in range(0, 5):
        unique_color_data = set()
        #print("next color")
        for color_column_indx in range(0, 5):
            tmp_data_v = board[8 - color_column_indx - color_row_indx][color_row_indx]
            tmp_data_h = board[8 - color_row_indx][color_row_indx + color_column_indx]
            if tmp_data_v.isnumeric():
                if int(tmp_data_v) in unique_color_data:
                    return False
                else:
                    unique_color_data.add(int(tmp_data_v))
            if tmp_data_h.isnumeric():
                if int(tmp_data_h) in unique_color_data:
                    return False
                else:
                    unique_color_data.add(int(tmp_data_h))
        #print(unique_color_data)

    return True


def validate_board(board: list) -> bool:
    """
    Check if board configuration for rows, columns and colors is valid.
    """
    if check_board_rows_and_cols(board):
        if check_board_color(board):
            return True

    return False


if __name__ == '__main__':
    board = [
        "**** ****",
        "***1 ****",
        "**  3****",
        "* 4 1****",
        "     9 5 ",
        " 6  83  *",
        "3   1  **",
        "  8  2***",
        "  2  ****"
    ]
    # Check if board configuration is valid and print result
    print(validate_board(board))
