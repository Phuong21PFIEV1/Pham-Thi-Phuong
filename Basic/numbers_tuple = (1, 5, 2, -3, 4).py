tuple_so = (1, 2, 3, 2, 1, 2)
gia_tri = 2


so_lan_xuat_hien = 0
for so in tuple_so:
  if so == gia_tri:
    so_lan_xuat_hien += 1



# In kết quả
print(f"Giá trị {gia_tri} xuất hiện {so_lan_xuat_hien} lần trong tuple.")