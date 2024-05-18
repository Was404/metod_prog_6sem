def assign_seats(S, N, seats):
    from collections import defaultdict

    row_counts = defaultdict(lambda: [0, 0])  # [males, females] for each row
    col_counts = defaultdict(lambda: [0, 0])  # [males, females] for each column
    assignment = [""] * N

    for index, (r, c) in enumerate(seats):
        males_in_row, females_in_row = row_counts[r]
        males_in_col, females_in_col = col_counts[c]

        # Prefer placing a male if it keeps the balance
        if (
            abs((males_in_row + 1) - females_in_row) <= 1
            and abs((males_in_col + 1) - females_in_col) <= 1
        ):
            assignment[index] = "M"
            row_counts[r][0] += 1
            col_counts[c][0] += 1
        elif (
            abs(males_in_row - (females_in_row + 1)) <= 1
            and abs(males_in_col - (females_in_col + 1)) <= 1
        ):
            assignment[index] = "W"
            row_counts[r][1] += 1
            col_counts[c][1] += 1
        else:
            return "Impossible"

    return "".join(assignment)


# Input handling
S, N = map(int, input().strip().split())
seats = [tuple(map(int, input().strip().split())) for _ in range(N)]

# Function call and output
result = assign_seats(S, N, seats)
print(result)
