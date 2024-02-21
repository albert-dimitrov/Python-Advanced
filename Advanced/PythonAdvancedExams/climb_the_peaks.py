from collections import deque

daily_portions = [int(x) for x in input().split(', ')]
quantity_of_daily_stamina = deque([int(x) for x in input().split(', ')])

conquered_peeks = []

peeks_data = deque([['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]])

while daily_portions and quantity_of_daily_stamina:
    daily_portion = daily_portions.pop()
    daily_stamina = quantity_of_daily_stamina.popleft()

    result = daily_portion + daily_stamina

    current_peek = peeks_data.popleft()

    if result >= current_peek[1]:
        conquered_peeks.append(current_peek[0])
    else:
        peeks_data.appendleft(current_peek)

    if not peeks_data:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peeks:
    print(f"Conquered peaks:", *conquered_peeks, sep='\n')