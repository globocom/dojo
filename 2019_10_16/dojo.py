class BuildStr:
    def __init__(self, answer, append_cost, copy_cost):
        self.answer = answer
        self.append_cost = append_cost
        self.copy_cost = copy_cost
        self.string = ''

    def append(self, str_):
        self.string += str_

    def find(self, str_):
        return str_ in self.string

    def pop_chars(self, chars):
        return self.answer[chars:]
