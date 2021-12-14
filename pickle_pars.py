import pickle
from my_pars import Pars


class PicklePars(Pars):

    def load(self, path):
        with open(path, 'rb') as file:
            obj = pickle.load(file)
        return obj

    def loads(self, str):
        return super().loads(pickle.loads(str))

    def dump(self, obj, path):
        with open(path, 'wb') as file:
            pickle.dump(obj, file)

    def dumps(self, obj):
        return pickle.dumps(super().dumps(obj))