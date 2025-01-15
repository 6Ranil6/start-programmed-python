import re
class Field(object):

    def __init__(self):
        self.table = dict()
    
    @staticmethod
    def reshape(key):

        if not isinstance(key, (tuple, str)):
            raise TypeError
        
        if type(key) == tuple: key = str(key[0]) + str(key[1])
        key = key.lower()

        re_key = re.findall(r'\w{1}\d+|\d+\w{1}', key)
 
        if len(re_key) != 1 or re_key[0] != key:
            raise ValueError
        
        if key[0].isdigit() and key[-1].isdigit():
            raise ValueError
        
        if key[0].isdigit(): key = key[-1] + key[:-1]

        return key

    def __setitem__(self, key, value):
        self.table[self.reshape(key)] = value

    def __getitem__(self, key):
        try:
            return self.table[self.reshape(key)]
        except:
            return None
    
    def __delitem__(self, key):
        del self.table[self.reshape(key)]

    def __contains__(self, key):
        return self.reshape(key) in self.table

    def __iter__(self):
        for value in self.table:
            yield self.table[value]
