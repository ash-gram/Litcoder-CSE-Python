def count_valid_splits(gold):
    if not all(isinstance(x, int) for x in gold):
        return "Input string was not in the correct format"

    total_gold = sum(gold)
    northern_gold = 0
    valid_splits = 0

    for i in range(len(gold) - 1):
        northern_gold += gold[i]
        southern_gold = total_gold - northern_gold

        if northern_gold >= southern_gold and southern_gold > 0:
            valid_splits += 1

    return valid_splits
try: 
    inp = input()
    inp = map(int ,inp.split())
    inp = list(inp)
    output_1 = count_valid_splits(inp)
    print( output_1)
except:
    print("Input string was not in the correct format")
