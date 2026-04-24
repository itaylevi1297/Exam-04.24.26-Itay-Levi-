Ranks = []
while True:
    user_input = input("enter rank:")

    try:
        rank = int(user_input)
    except ValueError:
        continue

    if rank == -999:
        if len(Ranks) >= 10:
            break
        else:
            continue
            
    if 1 <= rank <= 5:
        Ranks.append(rank)

avg_rank = sum(Ranks) / len(Ranks)
max_rank = max(Ranks)
valid_count = len(Ranks)

print("avg rank:", avg_rank)
print("max rank:", max_rank)
print("valid count:", valid_count)


