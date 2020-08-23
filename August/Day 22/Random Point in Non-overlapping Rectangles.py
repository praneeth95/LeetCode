import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        self.sum_=0
        
        for x1,y1,x2,y2 in rects:
            num_points = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.weights.append(num_points)
            self.sum_ += num_points
            
        self.weights = [x / self.sum_ for x in self.weights]

    def pick(self) -> List[int]:
        rectangle = random.choices(population = self.rects, weights = self.weights, k=1)[0]
        x1,y1,x2,y2 = rectangle 
        
        return[random.randint(x1,x2),random.randint(y1,y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()