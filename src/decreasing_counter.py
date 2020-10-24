class DecreasingCounter:
  value = 0
  def __init__(self,initial_value):
    self.value = initial_value

  def print_value(self):
    print("value: " + str(self.value))

  def reset(self):
    self.value = 0
    return self.value
  
  def decrement(self):
    self.value-=1
    if(self.value<0):
      self.reset()
      
    return self.value
        # write the method implementation here
        # the aim is to decrement the value of the counter by one

    # and the other methods go here
