from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

start_time = {
    'hour': int(config['start']['hour']),
    'minute': int(config['start']['minute']),
    'second': int(config['start']['second'])
}

end_time = {
    'hour': int(config['end']['hour']),
    'minute': int(config['end']['minute']),
    'second': int(config['end']['second'])
}

background = {
    'red': int(config['background']['red']),
    'green': int(config['background']['green']),
    'blue': int(config['background']['blue'])
}

resolution = {
    'width': int(config['resolution']['width']),
    'height': int(config['resolution']['height']),
}
