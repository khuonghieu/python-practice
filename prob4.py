import json
from modify_data import MODIFY_DATA
class StorefrontConfig:
    
    def __init__(self, data):
        self.data = data

    def update(self, modify_data):
        self.data = self.update_helper(self.data, modify_data)

    @classmethod
    def update_helper(cls, data, modify_data):
        for key, value in modify_data.items():
            #Call this func recursively if value is a dict
            if isinstance(value, dict):
                data[key] = cls.update_helper(data.get(key), value)
            else:
                data[key] = value
        return data

class FileController:
    
    @staticmethod
    def read_file(file_name):
        with open(file_name) as input_file:
            data = json.load(input_file)
        return StorefrontConfig(data)
    
    @staticmethod
    def write_file(data, file_name):
        with open(file_name, 'w') as output_file:
            output_file.write(json.dumps(data, indent=4))


file_controller = FileController()
config = file_controller.read_file('data.json')
config.update(MODIFY_DATA)
file_controller.write_file(config.data, 'result.json')