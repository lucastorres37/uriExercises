#1017

spent_time = int(input())
avrg_spd = int(input())

km_traveled = spent_time * avrg_spd

liters_needed = km_traveled / 12

print('%.3f' % liters_needed)