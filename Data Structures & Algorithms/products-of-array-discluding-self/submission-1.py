class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        straight_product = nums.copy()
        nums.reverse()
        reverse_product = nums.copy()
        
        
        print(reverse_product)
        for i in range(1,len(straight_product)):
            straight_product[i] = straight_product[i] * straight_product[i-1]
            reverse_product[i] = reverse_product[i] * reverse_product[i-1]

        reverse_product.reverse()
        print(reverse_product)
        output = []   
        output.append(reverse_product[1])    
        for i in range(1,len(nums)-1):
            output.append(straight_product[i-1] * reverse_product[i+1])

        output.append(straight_product[len(straight_product)-2])
        return output
