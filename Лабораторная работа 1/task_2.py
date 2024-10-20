# TODO Найдите количество книг, которое можно разместить на дискете

V = 1.44
pages = 100
st_on_page = 50
k_slo_in_st = 25

v_book_byte = 4 * k_slo_in_st * st_on_page * pages

v_book_Mb = v_book_byte/(1024**2)

count = int(V//v_book_Mb)

print("Количество книг, помещающихся на дискету:", count)