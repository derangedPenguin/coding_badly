'''len of bin(2**n) is n+1'''

class bitmap:
    def __init__(self, dims:tuple[int, int]) -> None:
        self.width = dims[0]
        self.height = dims[1]
        self.data = bin(2**(dims[0]*dims[1]))
    
    def get_str(self):
        output = ''
        for i, point in enumerate(str(self.data)[2:]):
            output += point
            if i % self.width == 0:
                output += '\n'
        return output


print(bitmap((8,8)).get_str())

