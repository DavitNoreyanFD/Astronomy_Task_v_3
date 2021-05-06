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
