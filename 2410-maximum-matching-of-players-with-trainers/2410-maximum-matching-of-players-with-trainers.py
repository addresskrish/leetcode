class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0 
        
        while trainers and players: 

            if players[-1] > trainers[-1]:
                players.pop()
                continue
            players.pop()
            trainers.pop()
            res += 1
        return res