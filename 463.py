# island perimeter

def island_perimeter(grid):
    island = 0
    for i in grid:
        for o in i:
            if o == 1:
                island += 1
    island_length = island * 4
    for i in grid:
        for o in range(len(i)-1):
            if i[o] == 1 and i[o+1] == 1:
                island_length -= 2
    change_direction = list(zip(*grid))
    for i in change_direction:
        for o in range(len(i)-1):
            if i[o] == 1 and i[o+1] == 1:
                island_length -= 2
    return island_length

if __name__ == '__main__':
    print(island_perimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))