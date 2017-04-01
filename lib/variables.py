class EnvironmentVariable(object):
    def __init__(self, item):
        self.name = item['name']
        self.version = item['version']
        self.value = item['value']

    def __str__(self):
        return self.name

    def to_shell_export(self):
        return 'export {}="{}"'.format(self.name, self.value)
