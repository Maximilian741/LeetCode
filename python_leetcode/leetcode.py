class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        #You may not use the same element twice.
        for i in range(Len(nums)):
            for j in range(i+1, Len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    #The arrow is stating that this is going to be a method that returns a boolean.
    def isPalindrome(self, x: int) -> bool:
        #An integer in a palindrome if it reads the ssame way forwards as it does backwards.
        if(x < 0):
            return False
        else:
            #Convert the integer to a string
            #str(x)
            #Reverse the string
            #str(x)[::-1]
            #Compare the two strings
            #== is a comparison operator
            #If they are the same, return true
            #If they are not the same, return false
            return str(x) == str(x)[::-1]
            
    def romanToInt(self, s: str) -> int:
        #Given a roman numeral, convert it to an integer.
        #Input is guaranteed to be within the range from 1 to 3999.
        #I = 1
        #V = 5
        #X = 10
        #L = 50
        #C = 100
        #D = 500
        #M = 1000
        #IV = 4
        #IX = 9
        #XL = 40
        #XC = 90
        #CD = 400
        #CM = 900
        #Create a dictionary to store the values of the roman numerals
        #The key is the roman numeral and the value is the integer
        #The key is a string and the value is an integer
        #The key is the roman numeral and the value is the integer
        
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #Create a variable to store the total
        total = 0
        #Loop through the string
        for i in range(len(s)):
            #Check if the current character is less than the next character
            if i > 0 and dict[s[i]] > dict[s[i-1]]:
                #If it is, subtract the current character from the total
                total += dict[s[i]] - 2 * dict[s[i-1]]
            else:
                #If it is not, add the current character to the total
                total += dict[s[i]]
        #Return the total
        return total

        def reverseInteger(self, x: int) -> int:
            #The code below does not work per the specified instructions.  This does indeed reverse the ordering of the inegers, however
            #it does not account for the fact that reversing the integer would remove it from it's 32 bit signed integer range.
            #which was specified in the directions.
            if x < 0:
                return -1 * int(str(-x)[::-1])
            else:
                return int(str(x)[::-1])

        #all i did here was add a check to see if the integer was within the 32 bit signed integer range.
        #this check will be performed in linear time, so it will not affect the overall time complexity of the algorithm.
        def reverseIntegerV2(self, x: int) -> int:
            if x.bit_length() > 31:
                return 0
            else:
                if x < 0:
                    return -1 * int(str(-x)[::-1])
                else:
                    return int(str(x)[::-1])

        #third attempt at the reverse intger problem.
        def reverseIntegerV3(self, x: int) -> int:
            #if the integer is negative, multiply it by -1 and then reverse it.
            #if the integer is positive, just reverse it.
            #if the reversed integer is greater than 2^31 - 1, return 0
            #if the reversed integer is less than -2^31, return 0
            #if the reversed integer is within the range, return the reversed integer
            if x < 0:
                reversedInteger = -1 * int(str(-x)[::-1])
            else:
                reversedInteger = int(str(x)[::-1])
            if reversedInteger.bit_length() > 31:
                return 0
            else:
                return reversedInteger

            #fuck this shit.  I'm done with this problem.
            #given a 32 bit signed integer, reverse the digits of the integer.
            #if the reversed integer is greater than 2^31 - 1, return 0
            #if the reversed integer is less than -2^31, return 0
            #if the reversed integer is within the range, return the reversed integer
            #if the integer is negative, multiply it by -1 and then reverse it.
            #if the integer is positive, just reverse it.
            def reverseIntegerV4(self, x: int) -> int:       
                if x.bit_length() > 31 & x.bit_length() < 0:
                    return 0
                elif x.bit_length() == 31:
                    return 0
                else:
                    if x < 0:
                        return -1 * int(str(-x)[::-1])
                    else:
                        return int(str(x)[::-1]) 

                        





        

