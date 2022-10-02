team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
red_cards = input().split()
game_is_terminated = False
for _ in range(len(red_cards)):
    for number in red_cards:
        if len(team_a) > 6 and len(team_b) > 6:
            if number in team_a:
                team_a.remove(number)
            elif number in team_b:
                team_b.remove(number)
        else:
            game_is_terminated = True
            break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_terminated:
    print("Game was terminated")


