import os
import hashlib
import yaml
import platform

class Data:
    def get_work_path(self):
        return self.get_path('work')

    def get_out_path(self):
        return self.get_path('out')

    def get_path_hash(self, key=''):
        return hashlib.md5(self.get_path(key).encode('utf-8')).hexdigest()

    def get_path(self, key=''):
        cwd = os.getcwd()
        default = cwd + "/" + key

        yaml_key = key + '_path'
        yaml_data = self.get_yml_data()

        if yaml_key in yaml_data:
            return cwd + '/' + yaml_data[yaml_key]

        return default

    def get_yml_data(self):
        file_path = os.getcwd() + "/AppImage.yml"

        stream = open(file_path, 'r')

        return yaml.load(stream)

    def architecture(self):
        arch = platform.architecture()[0]

        if arch == '64bit':
            return 'x86_64'

        return 'i686'
