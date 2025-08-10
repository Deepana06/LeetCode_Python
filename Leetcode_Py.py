#1.Create a DataFrame from List
import pandas as pd
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
#2.Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for i1 in range(i+1, len(nums)):
                if nums[i]+nums[i1] == target:
                    return [i,i1]
        
#9. Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        n1=[]
        for i in x:
            n1.append(i)
        
        if(n1[::-1]==n1):
            result= True
        else:
            result=False
        return result

#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)):
            if i<len(s) - 1 and d[s[i]] < d[s[i+1]]:
                result =result- d[s[i]]
            else:
                result =result+ d[s[i]]
        return result
        

#268. Missing Number
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        actual_sum=sum(nums)
        p_sums=n*(n+1)/2
        return (int((p_sums-actual_sum)))    
        
    
#448. Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
       
        n=len(nums)
        o_nums=set(range(1,n+1))
        return (list(set(o_nums)-set(nums)))  
        
#977. Squares of a Sorted Array
class Solution(object):
    def sortedSquares(self, nums):
        r=[]
        for i in nums:
            a=i*i
            r.append(a)
        r.sort()
        return(r)
            
        
#1266. Minimum Time Visiting All Points    
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        t=0
        for i in range(1,len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            dx=abs(x2-x1)
            dy=abs(y2-y1)
            t=t+max(dx,dy)
        return (t)
 #1365. How Many Numbers Are Smaller Than the Current Number
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        num=sorted(nums)
        index=[]
        sum=[]
        for i,n in enumerate(num):
            index.append(i)
            sum.append(n)
        result = []
        for n in nums:
            result.append(sum.index(n))
        return result

        

def maxProfit(self, prices):
    mn=0    

    filtered_prices = [price for price in prices if price != 0]

    if len(filtered_prices)>1 :
        mn=min(filtered_prices[:-1])
    else: 
        mn=min(filtered_prices)

    mn_ix=0
    for i in range(len(prices)):
        if(prices[i]==mn):
            #print("Index:", i, "Value:", prices[i])
            v2_i=i

    mn_ix=v2_i

    p=[]
    for v2_i in range(len(prices)):
        for v2_i_1 in range(v2_i+1,len(prices)):
            if(prices[v2_i]<prices[v2_i_1]):
                p.append(prices[v2_i_1])

    result=0
    if p : 
        result=max(p)-prices[mn_ix]
    else:
        0
    print(result)


#15 3 sum
class Solution(object):
    def threeSum(self, nums):
        a=[]
        for i in range(len(nums)):
            for i1 in range(i+1, len(nums)):
                for i2 in range(i1+1, len(nums)):
                    if(nums[i]+nums[i1]+nums[i2])==0:
                        a.append([nums[i],nums[i1],nums[i2]])
        
        return (a)
        
#54 spiral Matrix
 matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    min_col=0
    max_col=len(matrix[0])
    min_row=0
    max_row=len(matrix)
    result=[]
    row=0
#right to left moves from 0,0 to 0,4
    for column in range(min_col,max_col):
        result.append(matrix[row][column])
    min_row=min_row+1
# from top to down means 2,4 to 3,4
    for row in range(min_row, max_row):
        result.append(matrix[row][column])
    max_col=max_col-1
# from down to left 
    for column in range(max_col-1,min_col-1,-1):
        result.append(matrix[row][column])
    max_row=max_row-1
    for row in range(max_row-1, min_row-1,-1):
        result.append(matrix[row][column])
    min_col=max_col+1

    print(result)
    
 
#1200 Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
class Solution(object):
    def minimumAbsDifference(self, arr):
        d=0
        diff=[]
        for i in range(len(arr)):
            for i1 in range(i+1,len(arr)):
                d=arr[i]-arr[i1]
                diff.append(abs(d))
        min_val=min(diff)
        result=[]
        for i in range(len(arr)):
            for i1 in range(i+1,len(arr)):
                if(arr[i]-arr[i1]==int(min_val) or arr[i]-arr[i1]==int(-min_val)):
                    result.append([arr[i],arr[i1]])
                
        return(result)
            
        
           
#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)
        first_string=s[0]
        last_string=s[len(s)-1]
        common_string=[]

        i=0
        while i<len(first_string)+1:

            if first_string[0:i]==last_string[0:i]:
                common_string.append(first_string[0:i])
        
            i=i+1

        return (max(common_string))
        
#20. Valid Parentheses      
class Solution:
    def isValid(self, s: str) -> bool:
        r=[]
        result=True
        for i in s:
            if i=='(':
                r.append('(')
            elif i==')':
                if r and r[-1]=='(':
                    r.pop()
                else:
                    result=False
            elif i=='[':
                r.append('[')
            elif i==']':
                if r and r[-1]=='[':
                    r.pop()
                else:
                    result=False
            elif i=='{':
                r.append('{')
            elif i=='}':
                if r and r[-1]=='{':
                    r.pop()
                else:
                    result=False
        
        if r != [] or not result:
            result = False
        else:
            result = True

        return (result)
        
#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]

                j=j+1
    
        return j
  
# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=val:
                nums[j]=nums[i]

                j=j+1

        return(j)     

#28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        ix=[]

        for i in range(0,len(haystack)):
            if(haystack[i:i+n]==needle):
                ix.append(i)
        
        if ix==[]:
            ix1=-1
        else:
            ix1=min(ix)

        return(ix1)

#35. Search Insert Position   
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        i=0
        result_index=0
        
        for i in range(len(nums)):
            if nums[i]==target:
                result_index=i
                break

        return(result_index)
        
#58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.lstrip()
        s=s.rstrip()
        s=s[::-1]
        position=s.find(" ")
        r=[]
        if position>0:
            for i in range(0,position):
                r.append(s[i])
        else:
            for i in range(0,len(s)):
                r.append(s[i])
                
        return(len(r))

#66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit=""
        r=[]
        for i in range(len(digits)):
            digit=digit+str(digits[i])
        
        digit=int(digit)+1
        
        for i in str(digit):
            r.append(int(i))

        return(r)
        
#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        i=0
        n=len(s)
        right=0
        max_l=0

        while left<n:
            r=[]
            right=left
            while right<n and s[right] not in r:
                r.append(s[right])
                right=right+1

            max_l=max(max_l,right-left)
            left=left+1
        
        return(max_l)
#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        right=0
        left=0
        n=len(s)
        max_l=0
        r=[]
        p=""

        while left<n:
            right=left
            while right<n:
                r=s[left:right+1] 
                if r==r[::-1]and len(r)>max_l:
                    max_l=len(r)
                    p=r
                right=right+1
            left=left+1

        return (p)
        

                    
            