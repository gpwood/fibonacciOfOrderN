import sys
import numpy as np

class nmFib(object):
   def __init__(self, n=1, m=2, stop=10):
      assert n >= 0 and m >= 1
      self.steps = 0
      self.ratio = 0
      self.m = m
      self.n = n + 1
      self.stop = stop
      ones = np.ones(self.n+1)
      self.previous = ones.tolist()
      self.previous = list(map(int, self.previous))

   def nmFib(self):
      if self.stop  == self.steps:
        print(f"F({self.n}) ~ {self.ratio}")
        return self.ratio
      else:
        offset = -self.n + 1
        mysum = 1
        if offset == 0:
          mysum = sum(self.previous)
        else:
          mysum = sum(self.previous[:offset])
        self.ratio = mysum/self.previous[-1]
        self.steps = self.steps + 1
        offset = 2 - self.n
        if len(self.previous) >= self.m:
           if len(self.previous)+offset-self.m < 0:
             newarray = self.previous[slice(0,len(self.previous))]
             newarray.append(mysum)
             self.previous = newarray
           else:
             newarray = self.previous[slice(len(self.previous)+offset-self.m,len(self.previous))]
             newarray.append(mysum)
             self.previous = newarray
        else:
           self.previous.append(mysum)
        self.nmFib()

if __name__ == "__main__":
  sys.setrecursionlimit(10000)
  for n in range(0,100):
    for m in range(9999,10000):
      mypad = nmFib(n,m,8000)
      mypad.nmFib()

