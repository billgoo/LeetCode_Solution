class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if len(cpdomains) == 0:
            return cpdomains
        
        re = dict()
        for item in cpdomains:
            num, domains = int(item.split(" ")[0]), item.split(" ")[1].split(".")
            
            n = len(domains) - 1
            while n > 0:
                n -= 1
                domains[n] += "." + domains[n + 1]
            
            for d in domains:
                if d in re:
                    re[d] += num
                else:
                    re[d] = num
        
        result = []
        for key in re:
            result.append(str(re[key]) + " " + key)
        
        return result