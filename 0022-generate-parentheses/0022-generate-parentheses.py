class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl):
            if len(sol)==2*n:
                res.append("".join(sol))
                return
            if op<n:
                sol.append('(')
                backtrack(op+1,cl)
                sol.pop()
            if cl<op:
                sol.append(')')
                backtrack(op,cl+1)
                sol.pop()
        res,sol=[],[]
        backtrack(0,0)
        return res