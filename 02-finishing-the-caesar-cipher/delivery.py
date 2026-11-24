DAYS_IN_WEEK: int = 7

day: int = int(input("Day: "))
days_to_wait: int = int(input("Days to wait: "))

delivery_day: int = day + days_to_wait
if delivery_day > DAYS_IN_WEEK:
    delivery_day -= DAYS_IN_WEEK

print("Delivery day:", delivery_day)
assert 1 <= delivery_day <= DAYS_IN_WEEK