class padovan(object):
   def __init__(self,padtype=2, stop=10):
      self.steps = 0
      self.ratio = 0
      self.padtype = padtype
      self.stop = stop
      self.previous = [1, 1, 1]

   def padovan(self):
      if self.stop  == self.steps:
        print(f"Ratio {self.padtype}: {self.ratio}")
        return
      else:
        mysum = sum(self.previous[:-1])
        self.ratio = mysum/self.previous[-1]
        self.steps = self.steps + 1
        if len(self.previous) >= self.padtype:
           newarray = self.previous[slice(len(self.previous)-self.padtype,len(self.previous))]
           newarray.append(mysum)
           self.previous = newarray
        else:
           self.previous.append(mysum)
        self.padovan()

if __name__ == "__main__":
   for i in range(2,77):
      mypad = padovan(i,90)
      mypad.padovan()

