from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.indx=0
        self.length=combinationLength
        self.combos = [*combinations(characters,combinationLength)]

    def next(self) -> str:
        ans=''
        for char in self.combos[self.indx]:
            ans+=char
        self.indx+=1
        return ans

    def hasNext(self) -> bool:
         return self.indx < len(self.combos)        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()