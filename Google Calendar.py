from datetime import datetime, timedelta

seconds_in_day = 86400

current_date = int(datetime(*map(int, input("Enter current date (YYYY MM DD): ").split())).timestamp())
future_date = int(datetime(*map(int, input("Enter future date (YYYY MM DD): ").split())).timestamp())

number_of_days = (future_date - current_date) // seconds_in_day
graph = {}

for i in range(number_of_days):
    src = current_date + i * seconds_in_day
    for j in range(i + 1, number_of_days + 1):
        dst = current_date + j * seconds_in_day
        distance = (dst - src) // seconds_in_day
        graph.setdefault(src, []).append((dst, distance))

#pprint(graph)

def greedy_path(at_ts, to_ts):
    if at_ts > to_ts:
        print("Cannot go back in time.")
        return

    current = at_ts
    while current < to_ts:
        edges = graph.get(current, [])
        if not edges:
            print(f"No path from {datetime.fromtimestamp(current)}")
            return
        edges.sort(key=lambda x: x[1])
        next_day = edges[0][0]
        print(f"{datetime.fromtimestamp(current).strftime('%Y-%m-%d')} -> ", end="")
        current = next_day
    print(f"{datetime.fromtimestamp(to_ts).strftime('%Y-%m-%d')}")

greedy_path(current_date, future_date)