class Symbol:
    __plus = "+"
    __subtract = "-"
    __multiply = "*"
    __division = "/"
    __power = "^"
    __exegesis = "//"

    def __init__(self):
        pass

    def int(self, data) -> int:
        out = int(data)
        return out

    def float(self, data) -> float:
        out = float(data)
        return out
