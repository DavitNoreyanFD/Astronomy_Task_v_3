"""

"""
from random import randint
import datetime
import const_and_inp
import stars


def open_tsv(data_tsv, fov_ra: float, fov_dec: float, ra_user_input: float, dec_user_input: float) -> list:
    """
    in order not to load memory, the function checks if the star enters the field of view and then
    adds to array
    """
    fov_ra_min = ra_user_input - fov_ra / 2
    fov_ra_max = ra_user_input + fov_ra / 2
    fov_dec_min = dec_user_input - fov_dec / 2
    fov_dec_max = dec_user_input + fov_dec / 2
    try:
        with open(data_tsv) as fd:
            list_of_db = []
            index = 0
            for row in fd:
                index+=1
                list_row = row.split('\t')
                try:
                    if fov_ra_min < float(list_row[const_and_inp.INDEX_RA]) < fov_ra_max and \
                            fov_dec_min < float(list_row[const_and_inp.INDEX_DEC]) < fov_dec_max:
                        list_of_db.append(
                            stars.Star(
                                int(list_row[const_and_inp.INDEX_ID]),
                                float(list_row[const_and_inp.INDEX_RA]),
                                float(list_row[const_and_inp.INDEX_DEC]),
                                float(list_row[const_and_inp.INDEX_MAG])
                            )
                        )
                except ValueError:
                    if index > 2:
                        raise  Exception(f'there is an incorrectness in the database row. row index : {index}')
    except FileNotFoundError:
        raise Exception('not correct file path')

    return list_of_db


def quicksort(array: list, key, reverse: bool) -> list:

    if len(array) < 2:
        return array
    left = []
    same = []
    right = []
    delimiter = key(array[randint(0, len(array) - 1)], reverse)
    for item in array:
        if key(item, reverse) > delimiter:
            left.append(item)
        elif key(item, reverse) == delimiter:
            same.append(item)
        elif key(item, reverse) < delimiter:
            right.append(item)
    sorted_array = quicksort(left, key, reverse) + same + quicksort(right, key, reverse)
    return sorted_array


def n_high_mag(array: list, num: int) -> list:
    """
functions strips out num elements from array
    """
    return array[:num]


def my_key_mag(item, reverse: bool):
    if reverse is True:
        return -item.mag
    else:
        return item.mag


def my_key_dist(item, reverse: bool):
    if reverse is True:
        return -item.distance
    else:
        return item.distance


def create_result(star_array: list):
    """
the function is designed to create the final output as a .csv file,
the file name is the date and time of the current time
    """
    with open(f'{datetime.datetime.now()}.csv', 'w') as csv_temp:
        head = 'ID'.center(20) + ',' + \
               'RA'.center(20) + ',' + \
               'DEC'.center(20) + ',' + \
               'MAG'.center(20) + ',' + \
               'DISTANCE'.center(20) + '\n'
        csv_temp.write(head)
        for star in star_array:
            row = f'{star.id}'.center(20) + ',' + \
                  f'{star.ra}'.center(20) + ',' + \
                  f'{star.dec}'.center(20) + ',' + \
                  f'{star.mag}'.center(20) + ',' + \
                  f'{star.distance}'.center(20) + '\n'
            csv_temp.write(row)
