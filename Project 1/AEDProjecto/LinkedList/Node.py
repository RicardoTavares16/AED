#Adaptado dos slides da cadeira
class Node:
   def __init__(self, init_data, init_nick, init_years):
      self.data = init_data
      self.nick = init_nick
      self.years = init_years
      self.next = None
   def get_name(self):
      return self.data
   def get_nick(self):
      return self.nick
   def get_years(self):
      return self.years
   def get_next(self):
      return self.next
   def set_data(self, new_data):
      self.data = new_data
   def set_nick(self, new_nick):
      self.nick = new_nick
   def set_years(self, new_years):
      self.years = new_years
   def set_next(self, new_next):
      self.next = new_next