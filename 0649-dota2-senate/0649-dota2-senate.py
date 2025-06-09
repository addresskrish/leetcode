class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque()
        d_q = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] =='R':
                r_q.append(i)
            else:
                d_q.append(i)
        while len(r_q)!=0 and len(d_q)!=0:
            r = r_q.popleft()
            d = d_q.popleft()
            n+=1
            if r < d:
                r_q.append(n)
            else:
                d_q.append(n)
        if len(r_q) >0:
            return "Radiant"
        return "Dire"