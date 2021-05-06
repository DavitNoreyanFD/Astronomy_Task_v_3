"""
this is a working module where functions, stars modules are imported
"""

import const_and_inp
import functions


def main(data_path: str,
         fov_ra: float,
         fov_dec: float,
         ra_user: float,
         dec_user: float,
         vec_of_sort_mag: bool,
         vec_of_sort_dist: bool,
         num: int):
    """
a function that unites the work of all other work functions, it takes the following variables
    :param data_path: is the path of the file that contains the database
    :param fov_ra: is one of the parameters of the field of view
    :param fov_dec: is the second of the field of view parameters
    :param ra_user: is one of the coordinates of this direction Right ascension
    :param dec_user: is the second coordinate of the given direction Declination
    :param vec_of_sort_mag: is the star sorting vector based on brightness
    :param vec_of_sort_dist: is the vector to sort the stars based on the distance to the given point
    :param num: is the number of stars we will explore
    """
    filtered_data = functions.open_tsv(data_path, fov_ra, fov_dec, ra_user, dec_user)
    sorted_list_by_mag = functions.quicksort(filtered_data, functions.my_key_mag, reverse=vec_of_sort_mag)
    ob_list_n_high = functions.n_high_mag(sorted_list_by_mag, num)
    sorted_list_by_dist = functions.quicksort(ob_list_n_high, functions.my_key_dist, reverse=vec_of_sort_dist)
    functions.create_result(sorted_list_by_dist)


if __name__ == '__main__':
    main(const_and_inp.data_file,
         const_and_inp.fov_v,
         const_and_inp.fov_h,
         const_and_inp.ra_user,
         const_and_inp.dec_user,
         const_and_inp.vec_sort_mag,
         const_and_inp.vec_sort_dist,
         const_and_inp.n)
