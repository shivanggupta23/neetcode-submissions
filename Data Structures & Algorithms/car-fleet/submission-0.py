class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        prevtime=0
        for pos,sp in cars:
            time=(target-pos)/sp
            if time>prevtime:
                fleet+=1
                prevtime=time
        return fleet        