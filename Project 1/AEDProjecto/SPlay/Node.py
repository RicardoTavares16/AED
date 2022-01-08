#Adaptado dos slides da cadeira
class Node:
    def __init__(self, key, init_nick, init_years):
        self.key = key
        self.nick = init_nick
        self.years = init_years
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

    def get_name(self):
        return self.key

    def get_nick(self):
        return self.nick

    def get_years(self):
        return self.years

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.key = new_data

    def set_nick(self, new_nick):
        self.nick = new_nick

    def set_years(self, new_years):
        self.years = new_years