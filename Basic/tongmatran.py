matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0

for row in matrix:
  for number in row:
    total += number

print(f"Tổng các số trong ma trận là: {total}")