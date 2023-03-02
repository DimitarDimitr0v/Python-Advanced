eggs = [int(x) for x in input().split(", ")]
paper = [int(x) for x in input().split(", ")]

box_size = 50
filled_boxes = 0

while eggs and paper:

    egg_value = eggs[0]
    paper_value = paper[-1]

    # egg isn't fresh - remove
    if egg_value <= 0:
        eggs.remove(egg_value)
        continue

    # bad_luck_case - remove the egg_value and swap the paper first and last positions
    if egg_value == 13:
        eggs.remove(egg_value)

        temp = paper[0]
        paper[0] = paper[-1]
        paper[-1] = temp
        continue


    if egg_value + paper_value <= box_size:
        filled_boxes += 1
        eggs.remove(egg_value)
        paper.remove(paper_value)
    else:
        eggs.remove(egg_value)
        paper.remove(paper_value)

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper])}")