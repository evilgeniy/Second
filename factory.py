from json_pars import JsonPars
from toml_pars import TomlPars
from pickle_pars import PicklePars
from yaml_pars import YamlPars


class Factory():

    @staticmethod
    def factory(typename):
        if typename == 'Json':
            return JsonPars()
        elif typename == 'Toml':
            return TomlPars()
        elif typename == 'Pickle':
            return PicklePars()
        elif typename == 'Yaml':
            return YamlPars()
