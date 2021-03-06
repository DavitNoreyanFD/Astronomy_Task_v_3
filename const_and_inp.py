"""
All constants and imported variables were collected in this module.
"""

import configparser


config = configparser.ConfigParser()
config.read('config.ini')
data_file = config['USER']['data_file']


try:
    fov_v = float(config['USER']['fov_v'])
    fov_h = float(config['USER']['fov_h'])
    ra_user = float(config['USER']['ra_user'])
    dec_user = float(config['USER']['dec_user'])
    vec_sort_mag = int(config['USER']['vec_sort_mag']) != 0
    vec_sort_dist = int(config['USER']['vec_sort_dist']) != 0
    n = int(config['USER']['n'])
    if n < 1:  # condition checks the value of n so that the script does not start working if there is no object to use
        raise Exception('the number of stars must be greater than Zero for the script to work')
except ValueError:
    raise Exception('invalid variable')


INDEX_ID = 7
INDEX_RA = 0
INDEX_DEC = 1
INDEX_MAG = 22
INDEX_FLUX = 20
