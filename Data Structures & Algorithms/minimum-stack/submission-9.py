class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            last_el = self.mins[-1]
            if val == last_el:
                self.mins.append(val)
            else:
                min_el = min(last_el, val)
                if min_el != last_el:
                    self.mins.append(min_el)
        

    def pop(self) -> None:
        el = self.stack.pop()
        if el == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
