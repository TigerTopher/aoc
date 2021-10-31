def computeSeatId(boarding_pass):
  row_count = 128
  row_start = 0
  row_end = 127

  column_count = 8
  column_start = 0
  column_end = 7

  for c in boarding_pass:
    row_count = (row_end - row_start + 1)
    column_count = (column_end - column_start + 1)

    if c == "F":
      row_start = row_start
      row_end = row_end - (row_count/2)
    elif c == "B":
      row_start = row_start + (row_count/2)
      row_end = row_end
    elif c == "R":
      column_start = column_start + (column_count/2)
      column_end = column_end
    elif c == "L":
      column_start = column_start
      column_end = column_end - (column_count/2)

  row = row_start if row_start == row_end else 0
  column = column_start if column_start == column_end else 0

  return (row * 8) + column

boarding_passes = []
maximum_seat = 0

for x in open("input.txt", "r"):
  line = x.strip()

  boarding_passes.append(line)
  value = computeSeatId(line)

  if value > maximum_seat:
    maximum_seat = value

print(maximum_seat)
