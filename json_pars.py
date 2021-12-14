import json
from my_pars import Pars
import re


class JsonPars(Pars):

    tuples = ['co_consts', 'co_names', 'co_freevars', 'co_cellvars']
    lists = ['nlocals', 'co_code', 'co_lnotab', 'co_varnames']

    def dumps_wrapper(self, obj):
        json_str = '{\n'
        for key in obj:
            if isinstance(obj[key], dict):
                temp = self.dumps_wrapper(obj[key])
                if key == list(obj.keys())[-1]:
                    end = '\n'
                else:
                    end = ',\n'
                json_str += "\"" + key + "\"" + ": " + temp + end
                continue
            elif isinstance(obj[key], list) or isinstance(obj[key], tuple):
                json_str += "\"" + key + "\"" + ": ["
                for i in range(len(obj[key])):
                    if isinstance(obj[key][i], str):
                        json_str += "\"" + obj[key][i] + "\", "
                    elif isinstance(obj[key][i], int):
                        json_str += str(obj[key][i]) + ", "
                if json_str.endswith(", "):
                    json_str = json_str[: len(json_str) - 2] + "],\n"
                else:
                    json_str += "],\n"
            elif isinstance(obj[key], str):
                json_str += "\"" + key + "\"" + ": " + "\"" + obj[key].replace('\\', '\\\\') + "\"" + ",\n"
            elif isinstance(obj[key], int):
                json_str += "\"" + key + "\"" + ": " + str(obj[key]) + ",\n"

            elif isinstance(obj[key], type(None)):
                json_str += "\"" + key + "\"" + ": " + 'null' + ",\n"

            if key is list(obj.keys())[-1]:
                json_str = json_str[: len(json_str) - 2]
                json_str += '\n'

        if json_str.endswith(",\n"):
            json_str = json_str[:(len(json_str) - 2)] + "}"
        else:
            json_str += "}"
        return json_str

    def dumps(self, obj):
        obj = super().dumps(obj)
        return self.dumps_wrapper(obj)

    def loads(self, json_str):
        if 'code' in json_str:
            return super().loads(self.json_to_function(json_str));
        else:
            return super().loads(self.json_to_object(json_str));

    def str_to_collection(self, string):
        string = string.replace('[', '').replace(']', '')
        lst = string.split(' ')
        listvalue = []
        for item in lst:
            if isinstance(item, str):
                if item.isdigit():
                    value = int(item)
                    listvalue.append(value)
                else:
                    if item != '':
                        listvalue.append(item)
        return listvalue

    def json_to_function(self, json_str):
        json_str = json_str.replace("},\n\"globals\"", "}\n\"globals\"")
        string = re.sub('[{}\"]', '', json_str)
        lst = string.split('\n')
        code = {}
        glob = {}
        lst = [item for item in lst if not item == '']
        for item in lst:
            pair = item.split(': ')
            pair[1] = re.sub('[,]', '', pair[1])
            if pair[0] == 'code' or pair[0] == 'globals':
                continue
            if pair[0] in self.tuples or pair[0] in self.lists:
                value = self.str_to_collection(pair[1])
            else:
                if isinstance(pair[1], str):
                    if pair[1].isdigit():
                        value = int(pair[1])
                    else:
                        value = pair[1]
            if pair[0].startswith('co_'):
                code[pair[0]] = value
            else:
                glob[pair[0]] = value
        func = {'code': code, 'globals': glob}
        return func

    def json_to_object(self, json_str):
        string = re.sub('[{}\"]', '', json_str)
        lst = string.split('\n')
        glob = {}
        lst = [item for item in lst if not item == '']
        for item in lst:
            pair = item.split(': ')
            pair[1] = re.sub('[,]', '', pair[1])
            if pair[0] == 'code' or pair[0] == 'globals':
                continue
            if isinstance(pair[1], str):
                if pair[1].isdigit():
                    value = int(pair[1])
                else:
                    value = pair[1]

            glob[pair[0]] = value
        return glob