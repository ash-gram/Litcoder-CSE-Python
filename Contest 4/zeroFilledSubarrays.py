def zeroFilledSubarray(nums):

        def sumOfIntegers(num):
            return num*(1 + num)//2

        res = zeros = 0
        for i in nums:
            if i != 0: 
                res += sumOfIntegers(zeros)
                zeros = 0
                continue
            zeros += 1
                
        return res if not zeros else res + sumOfIntegers(zeros)

inp = input()
inp = map(int ,inp.split())
inp = list(inp)
output_1 = zeroFilledSubarray(inp)
print( output_1)