def calculate_batting_avg(hits, atbats):
    batavg = hits / atbats
    return batavg

count = 0
hits = 0
atbats = 0
for count in range(1,10,1):
    print("Enter a name ")
    name = input()
    print("Enter number of hits ")
    hits = int(input())
    print("Enter number of at bats ")
    atbats = int(input())
    batavg = calculate_batting_avg(hits, atbats)
    print("Player " + name + " has a batting average of " + str(batavg))
print("Total number of players: ", count)