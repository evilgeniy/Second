import toml
from my_pars import Pars

class TomlPars(Pars):

    def dumps(self, obj):
        obj_dict = super().dumps(obj)
        if 'code' in obj_dict:
            for (key, value) in obj_dict['code'].items():
                if key == 'co_consts':
                    value = list(value)
                    obj_dict['code'][key] = value
        return toml.dumps(obj_dict )

    def loads(self, string):
        return super().loads(toml.loads(string))