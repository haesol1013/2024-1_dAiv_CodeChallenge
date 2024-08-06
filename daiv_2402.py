w_x, w_y = map(int, input().split())
b_x, b_y = map(int, input().split())

x_diff = abs(w_x-b_x) % 2
y_diff = abs(w_y-b_y) % 2

result = "black" if x_diff + y_diff == 2 else "white"
print(result)
