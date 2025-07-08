wheel, car_body, figure = map(int, input().strip().split())

w = wheel // 4
cb = car_body // 1
f = figure // 2

cars = min(w, cb, f)
print(cars)