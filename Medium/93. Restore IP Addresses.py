class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        ans = []
        
        for i in range(4):
            ip1 = s[:i]
            if not ip1 or int(ip1) > 255: continue
            if len(ip1) != len(str(int(ip1))): continue
        
            for j in range(i+1,i+4):
                ip2 = s[i:j]
                if not ip2 or int(ip2) > 255: continue
                if len(ip2) != len(str(int(ip2))): continue
            
                for k in range(j+1,j+4):
                    ip3 = s[j:k]
                    if not ip3 or int(ip3) > 255: continue
                    if len(ip3) != len(str(int(ip3))): continue
                
                    for l in range(k+1,k+4):
                        ip4 = s[k:l]
                        if not ip4 or int(ip4) > 255: continue
                        if len(ip4) != len(str(int(ip4))): continue    
                    
                        if len(s) == l:
                            ans.append(ip1 + '.' + ip2 + "." + ip3 + '.' + ip4)
    
        return ans