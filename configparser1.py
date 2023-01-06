import configparser

config = configparser.ConfigParser()

config.read('example.cfg')
print(config.sections())

for key in config['SectionTwo']:
    value = config['SectionTwo'][key]
    print("{0} : {1}".format(key,value))
