def solve(numheads, numlegs):
    chikens = (numlegs - (4 * numheads)) / -2
    rabits = numheads - chikens
    return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}"

# print(solve(35, 94)) 
#asnwer: Rabits: 12
#        Chikens: 23
