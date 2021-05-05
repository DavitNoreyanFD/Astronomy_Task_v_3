"""

"""
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

