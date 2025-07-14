class Queen:
    BOARD_SIZE = 7

    def __init__(self, row: int, column: int):
        if not isinstance(row, int) or not isinstance(column, int):
            raise TypeError("Row and column must be integers.")

        if row < 0:
            raise ValueError("row not positive")

        if row > self.BOARD_SIZE:
            raise ValueError("row not on board")

        if column < 0:
            raise ValueError("column not positive")

        if column > self.BOARD_SIZE:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen: "Queen") -> bool:
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if self.row == another_queen.row:
            return True

        if self.column == another_queen.column:
            return True

        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        return False
