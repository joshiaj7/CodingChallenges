# leetcode

import re

class Solution:
    def checkIPv4(self, IPs: List[str]) -> str:
        regex = "[^0123456789]+"
        if len(IPs) != 4:
            return "Neither"
        
        for i in IPs:
            if len(i) == 0:
                return "Neither"
            if len(i) > 1 and i[0] == '0':
                return "Neither"
            
            x = re.findall(regex, i)
            if len(x) > 0:
                return "Neither"
            elif int(i) > 255:
                return "Neither"
        return "IPv4"
        
    def checkIPv6(self, IPs: List[str]) -> str:
        regex = "[^1234567890abcdef]+"
        
        if len(IPs) != 8:
            return "Neither"
        
        for i in IPs:
            if len(i) == 0 or len(i) > 4:
                return "Neither"
            x = re.findall(regex, i.lower())
            if len(x) > 0:
                return "Neither"

        return "IPv6"
    
    
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            return self.checkIPv4(IP.split("."))
        elif ":" in IP:
            return self.checkIPv6(IP.split(":"))
        else:
            return "Neither"        
        