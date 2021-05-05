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
    with open(data_tsv) as fd:
        list_of_db = []
        for row in fd:
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
                pass

        return list_of_db


def quicksort(array: list, key) -> list:

    if len(array) < 2:
        return array
    left = []
    same = []
    right = []
    delimiter = key(array[randint(0, len(array) - 1)])
    for item in array:
        if key(item) > delimiter:
            left.append(item)
        elif key(item) == delimiter:
            same.append(item)
        elif key(item) < delimiter:
            right.append(item)
    sorted_array = quicksort(left, key) + same + quicksort(right, key)
    return sorted_array


def n_high_mag(array: list, num: int) -> list:
    """
functions strips out num elements from array
    """
    return array[:num]


def my_key_mag(item, reverce: bool):
    if reverce is True:
        return -item.mag
    else:
        return item.mag



def my_key_dist(item, reverce: bool):
    if reverce is True:
        return -item.distance
    else:
        return item.distance


