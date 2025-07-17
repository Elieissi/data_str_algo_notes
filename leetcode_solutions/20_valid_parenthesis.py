class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        dit = {')':'(', ']':'[', '}':'{'} 
        for char in s: #for each character in the string
            if char in dit.values(): #if the character is an opener
                stack.append(char) #add it to stack of stuff to fix
            
            elif char in dit: #if its a closer
                if not stack or stack[-1] != dit[char]: #If the stack is empty, or the current closer doesnt map to the most recent opener on the stack according to the dictionary
                    return False #its automatically false
            
                stack.pop() #otherwise, match the closer to the opener and remove it from the stack
        return not stack #if the stack is empty, this means that match was found for everything. Return True. Otherwise return false.