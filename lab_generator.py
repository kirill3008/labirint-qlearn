from copy import deepcopy
from random import uniform







def no_botom_in_group(group_n,line,i):
    line.pop(i)
    for item in line:
        if item[0] == group_n and item[1]["Down"]:
            return True
    return False

def create_maze(maze_size,wall_chance = (0.5,0.5)):
    width = maze_size[0]
    height = maze_size[1]
    vertical_wall_chance = wall_chance[0]
    horizontal_wall_chance = wall_chance[1]

    line = [[i,{'Left':True,'Right':True,'Up':True,'Down':True}] for i in range(width)]
    matrix = []
    

    for line_num in range(height):
        line = deepcopy(line)

        #delete group id under botom walls
        for i in range(len(line)):
            if not line[i][1]["Down"]:
                line[i][0] = i+line_num*width
            line[i][1] = {'Left':True,'Right':True,'Up':True,'Down':True}
        cur_line = line


        #add walls betwen same groups and add some random
        for i in range(width-1):
            if cur_line[i][0] == cur_line[i+1][0]:
                cur_line[i][1]["Right"] = False
                cur_line[i+1][1]["Left"] = False
            elif uniform(0,1) > vertical_wall_chance:
                cur_line[i][1]["Right"] = False
                cur_line[i+1][1]["Left"] = False
            else:
                cur_line[i+1][0] = cur_line[i][0]

        #add bottom walls if not all have 
        for i in range(width):
            if uniform(0,1) > horizontal_wall_chance and no_botom_in_group(cur_line[i][0],deepcopy(cur_line),i):
                cur_line[i][1]["Down"] = False

        #add up walls if there is bottom wall in prev line
        for i in range(width):
            if line_num>0 and matrix[line_num-1][i][1]["Down"] == False:
                cur_line[i][1]["Up"] = False

        matrix.append(cur_line)
        line = cur_line

    #conect different part in last lines
    for i in range(width-1):
        if matrix[-1][i][0] != matrix[-1][i+1][0]:
            matrix[-1][i][1]["Right"] = True
            matrix[-1][i+1][1]["Left"] = True
    #add maze borders
    for i in range(width):
        matrix[-1][i][1]["Down"] = False
        matrix[0][i][1]["Up"] = False
    for i in range(height):
        matrix[i][0][1]["Left"] = False
        matrix[i][-1][1]["Right"] = False

    #clear part numes
    for i in range(height):
        for j in range(width):
            matrix[i][j] = matrix[i][j][1]


    return matrix


def printer(matrix):
    ans = []
    for i in matrix:
        l1 = ''
        l2 = ''
        l3 = ''
        for j in i:
            if not j["Up"]:
                l1 += " - "
            else:
                l1 += "   "
            if not j["Down"]:
                l3 += " - "
            else:
                l3 += "   "
            if not j["Left"]:
                l2 += "|"
            else:
                l2 += " "
            l2 += " "
            if not j["Right"]:
                l2 += "|"
            else:
                l2 += " "
        ans.append(l1)
        ans.append(l2)
        ans.append(l3)

    print('\n'.join(ans))






printer(create_maze((3,3)))
