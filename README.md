**Task for exploring the stars**

The work of the script is as follows - The script takes the path of the
.tsv file, view parameters, a specific direction in the sky and the number
of stars, and as a result produces a list of the brightest stars sorted by
distance from a given point.

Variables are imported into the script using the config.ini file where the following variables are present

data_file is the path of the file that contains the database

fov_v is one of the parameters of the field of view, in the script it is in accordance with the direction of Right ascension

fov_h is the second of the field of view parameters, in the script it is in accordance with the Declination direction

ra_user is one of the coordinates of this direction Right ascension

dec_user is the second coordinate of the given direction Declination

n is the number of stars we will explore. If n is not enough 1, then the script will not work and throws exceptions

vec_sort_mag is the star sorting vector based on brightness. this variable can take 2 values ​​0 and 1.0 if we
want to sort from large to small and 1, respectively, to sort from small to large

vec_sort_dist is the vector to sort the stars based on the distance to the given point. this variable can take 2 
values ​​0 and 1.0 if we want to sort from large to small and 1, respectively, to sort from small to large

for the correct use of the script, please fill in all the values of the variables correctly