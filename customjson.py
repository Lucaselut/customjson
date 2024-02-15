import json as js, os

class json:
    __class__ = dict
    def __init__(self, data={}):
        if isinstance(data, dict):
            self.__data__ = data
        else:
            if os.path.exists(data):
                self.__data__ = js.load(open(data,'rb'))
            else:
                self.__data__ = js.loads(data)
    
    def __getattr__(self, name):
        if not name in self.__data__: return None
        if isinstance(self.__data__[name], dict):
            return json(self.__data__[name])
        return self.__data__[name]
    
    def __type__(self):
        return dict
    
    def __getitem__(self, name):
        return self.__getattr__(name)
    
    def __setattr__(self, name, val):
        if name == '__data__' and isinstance(val, dict):
            object.__setattr__(self, name, val)
        else:
            self.__data__[name] = val
    
    def __delitem__(self, name):
        if name in self.__data__:
            del self.__data__[name]
    
    def __delattr__(self, name):
        if name in self.__data__:
            del self.__data__[name]    
        
    def __setitem__(self, name, val):
        self.__data__[name] = val
    
    def __str__(self):
        return js.dumps(self.__data__)
    
    def __dir__(self):
        return sorted(list(self.__data__))
    
    def __len__(self):
        return len(self.__data__)
    
    def __add__(self, data):
        orig = self.__data__.copy()
        if isinstance(data, dict):
            for val in data:
                self.__data__[val] = data[val]
        elif isinstance(data, str):
            self.__data__[data] = None
        elif isinstance(data, int):
            self.__data__[data] = None
        elif isinstance(data, list):
            for name in data:
                self.__data__[name] = None
        retr = self.__data__.copy()
        self.__data__ = orig.copy()
        return json(retr)
    
    def __sub__(self, data):
        orig = self.__data__.copy()
        if isinstance(data, dict):
            for val in data:
                if val in self.__data__ and self.__data__[val] == data[val]:
                    del self.__data__[val]
        elif isinstance(data, str):
            if data in self.__data__:
                del self.__data__[data]
        elif isinstance(data, int):
            if data in self.__data__:
                del self.__data__[data]
        elif isinstance(data, list):
            for name in data:
                if name in self.__data__:
                    del self.__data__[name]
        retr = self.__data__.copy()
        self.__data__ = orig.copy()
        return json(retr)
    
    def __repr__(self):
        return str(self.__data__)
    
    def __dict__(self):
        return self.__data__
    
    def __eq__(self, data):
        return self.__data__ == data
    
    def __call__(self, name):
        return self.__getattr__(name)
        
    # base dict keys
    
    def copy(self):
        return self.__data__.copy()
    
    def clear(self):
        self.__data__.clear()
   
    def fromkeys(self, *args):
        return json(dict.fromkeys(*args))
    
    def get(self, name, a=None):
        if self.__getitem__(name) == None:
            if isinstance(a, dict):
                return json(d)
            return a
        else:
            return self.__getitem__(name)
    
    def items(self):
        d = []
        for val in self.__data__:
            d.append((val, self.__data__[val]))
        return d
    
    def keys(self):
        return list(self.__data__)
    
    def pop(self, name):
        val = None
        if name in self.__data__:
            val = self.__data__[name]
            del self.__data__[name]
        return val
    
    def popitem(self):
        if len(self.__data__) == 0: return None
        itm = list(self.__data__)[len(self.__data__)-1]
        val = self.__data__[itm]
        del self.__data__[itm]
        return (itm, val)
    
    def setdefault(self, name, val):
        if name in self.__data__: self.__data__[name] = val
        return self.__data__[name]
   
    def update(self, ary):
        d = self.__add__(ary)
        self.__data__ = d.__data__.copy()
    
    def values(self):
        d = []
        for v in self.__data__:
            d.append(self.__data__[v])
        return d