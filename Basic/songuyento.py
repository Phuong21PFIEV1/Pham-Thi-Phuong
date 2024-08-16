n = int(input("Nhập giá trị n: "))

if n < 2:
  print(f"{n} không phải là số nguyên tố")
  exit()

# Lặp từ 2 đến n-1
for i in range(2, n):
  # Chia n cho i
  if n % i == 0:
    print(f"{n} không phải là số nguyên tố")
    exit()

# n là số nguyên tố
print(f"{n} là số nguyên tố")