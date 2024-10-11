# TODO Найдите количество книг, которое можно разместить на дискете
const = 1024
disk = float(1.44)
disk_in_bite = 1.44 * const * const
stran = 100
strok = 50
sim = 25
sim_bite = 4
sim_na_stran = sim * strok
sim_v_knige = sim_na_stran * stran
bite_v_knige = sim_bite * sim_v_knige
max_book = int(disk_in_bite // bite_v_knige)
print("Количество книг, помещающихся на дискету:", max_book)
