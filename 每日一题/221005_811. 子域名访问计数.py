import collections
from typing import List


class Solution:
    def getdomain(self, dom: str) -> List[str]:
        ans = []
        sp = dom.split('.')
        for i in range(len(sp)):
            ans.append('.'.join(sp[i:]))
        return ans
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = collections.defaultdict(int)
        for domain in cpdomains:
            num, dom = domain.split(' ')
            doms = self.getdomain(dom)
            for d in doms:
                cnt[d] += int(num)
        ans = []
        for k, v in cnt.items():
            tmp = str(v) + " " + k
            ans.append(tmp)
        return ans