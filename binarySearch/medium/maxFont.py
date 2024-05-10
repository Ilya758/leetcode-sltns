class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: list[int], fontInfo : 'FontInfo') -> int:
        def isFeasible(fs):
            a = 0

            for char in text:
                a += fontInfo.getWidth(fs, char)  
            
            b = fontInfo.getHeight(fs)

            return a <= w and b <= h

        left, right = 0, len(fonts) - 1

        while left <= right:
            mid = (left + right) >> 1

            if isFeasible(fonts[mid]):
                left = mid + 1
            else:
                right = mid - 1 
    
        return -1 if right == -1 else fonts[right]
    
