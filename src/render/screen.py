class Screen:
    def __init__(self, width: int, height: int, cell_height: int, fill=' '):
        self.fill = fill

        self.width = width
        self.height = height

        self.cell_height = cell_height
        self.cell_width = cell_height * 3 // 5

        self.cols = width // self.cell_width
        self.rows = height // self.cell_height

        self.grid = [
            [self.fill] * self.cols
            for _ in range(self.rows)
        ]

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @property
    def rectangle(self) -> tuple[int, int, int, int]:
        return 0, 0, self.width - 1, self.height - 1

    def write(self, col: int, row: int, text: str):
        assert 0 <= col < self.cols
        assert 0 <= row < self.rows

        text_width = len(text)
        assert text_width + col < self.cols

        for i, ch in enumerate(text):
            self.grid[row][col + i] = ch

    def write_reverse(self, last_col: int, row: int, text: str):
        assert 0 <= last_col < self.cols
        assert 0 <= row < self.rows

        text_width = len(text)
        col = last_col + 1 - text_width
        assert col >= 0

        for i, ch in enumerate(text):
            self.grid[row][col + i] = ch
