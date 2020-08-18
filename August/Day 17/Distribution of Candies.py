class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        x=0
        candy_list = [0] * num_people
        
        while candies > 0:
            candy_list[x % num_people] += min(x+1, candies)
            x +=1
            candies -=x
        return candy_list
        