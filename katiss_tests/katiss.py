class katiss_sim:
    def __init__(self, input_list) -> None:
        self.input_list = list(input_list)

    def inp(self):
        return self.input_list.pop(0)
    
    def odd_echo(self):
        for i in range(self.inp()):
            if i % 2 == 0:
                print(self.inp())
            else:
                self.inp()

katiss_sim([10, 'only', 'if', 'these', 'oddindexed', 'words', 'appear', 'are', 'you', 'correct', 'output']).odd_echo()
list.reverse