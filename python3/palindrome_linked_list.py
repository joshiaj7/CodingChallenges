from .model import ListNode

# Space : O(n) 
# Time  : O(n)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
            mem = []

            p = head
            while p:
                mem.append(p.val)
                p = p.next
                
            s, e = 0, len(mem)-1
            while s < e:
                if mem[s] != mem[e]:
                    return False
                s += 1
                e -= 1
            
                
            return True