number_of_rooms = int(input())
total_chairs = 0
total_visitors = 0
for room in range(1, number_of_rooms + 1):
    chairs_visitors = input().split()
    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])
    total_chairs += chairs
    total_visitors += visitors
    if visitors > chairs:
        difference = visitors - chairs
        print(f"{difference} more chairs needed in room {room}")

total_difference = total_chairs - total_visitors
if total_chairs >= total_visitors:
    print(f"Game On, {total_difference} free chairs left")

