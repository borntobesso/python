class TinyStatistician:
    def mean(self, x):
        if len(x) == 0:
            return None
        sum = 0
        for i in x:
            sum += i
        return sum / len(x)
    
    def median(self, x):
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        else:
            return float(x[len(x) // 2])
        
    def quartiles(self, x):
        if len(x) == 0:
            return None
        x.sort()
        q1_index = int(len(x) * 0.25)
        q3_index  = int(len(x) * 0.75)
        
        return [float(x[q1_index]), float(x[q3_index])]
    
    def var(self, x):
        if len(x) == 0:
            return None
        mean = self.mean(x)
        sum = 0
        for i in x:
            sum += (i - mean) ** 2
        return sum / len(x)
    
    def std(self, x):
        if len(x) == 0:
            return None
        return self.var(x) ** 0.5
    
if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartiles(a))
    print(tstat.var(a))
    print(tstat.std(a))
    print(tstat.mean([]))
    print(tstat.median([]))
    print(tstat.quartiles([]))
    print(tstat.var([]))
    print(tstat.std([]))