def can_sit_together(seating_arrangement, person, table):
    for p, t in seating_arrangement:
        if p == person and t == table:
            return False
    return True

def main():
    N, M = map(int, input().split())
    cannot_sit_together = [tuple(map(int, input().split())) for _ in range(M)]
    
    seating_arrangement = []
    table1 = []
    table2 = []

    for person in range(1, N+1):
        if all(can_sit_together(seating_arrangement, person, table) for table in table1):
            table1.append(person)
            seating_arrangement.append((person, 1))
        elif all(can_sit_together(seating_arrangement, person, table) for table in table2):
            table2.append(person)
            seating_arrangement.append((person, 2))
        else:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, table1)))
    print(" ".join(map(str, table2)))

if __name__ == "__main__":
    main()
