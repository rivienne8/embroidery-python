import math



def draw_rectangle(width, height,border_color = 1,fill_color = 1, border_width = 1):
    matrix = []
    for i in range(0,height):
        # if i in range(:border_width):
        row = []
        for j in range(0,width):
            if i in list(range(0,height))[:border_width] or\
               i in list(range(0,height))[- border_width:]:
                row.append(border_color)

            else:
                if j in list(range(0,width))[:border_width] or\
                   j in list(range(0,width))[-border_width:]:
                    row.append(border_color)
                else:
                    row.append(fill_color) 
        matrix.append(row)
    return matrix


def draw_triangle(height,border_color = 1,fill_color = 1,border_width=1):
    matrix = []
    width = height*2-1
        
    # middle = [width // 2+1]
    middle = [width //2] # //2 a nie //2+1  bo zaczynamy indeksowanie od 0 w width
    k = 1
    for i in range(0,height):
        row = []
        for j in range(0,width): 
            if i <border_width or i >= height - border_width:                   
                if j in middle :
                    row.append(border_color)
                else:
                    row.append(0)
            else:
                if j in middle:
                    if j== min(middle) or j == max(middle):
                        row.append(border_color)
                    else:
                        row.append(fill_color)
                else:
                    row.append(0)    
            

        middle += [middle[0] + k, middle[0] -k]
        k += 1
        matrix.append(row) 
        
          
        
    return matrix


def draw_christmas_tree(blocks, border_color=1, fill_color=1):
    matrix = []

    b_height = 3
    width = (3*2-1) +blocks*2-2
    height = blocks *3

    middle = [width //2]
    count = 0
    k = 1
    while count < blocks:
        for i in range(0,b_height):
            row = []
            for j in range(0,width):
                if (count == 0 and i <1) or (count == blocks -1 and i == b_height-1):
                    if j in middle:
                        row.append(border_color)                    
                    else:
                        row.append(0)
                else:
                    if j in middle:
                        if j == max(middle) or j == min(middle):
                            row.append(border_color)
                        else:
                            row.append(fill_color)
                    else:
                        row.append(0)
            matrix.append(row) 
            if i != b_height-1:
                middle += [middle[0]+k,middle[0]-k]
                k += 1
  
        k -= 1
        count += 1                              
        middle.remove(min(middle))
        middle.remove(max(middle))

    return matrix
    
def draw_circle(radius, border_color=1,fill_color = 1):
    matrix = []
    

    width = radius*2
    height = radius*2

    for i in range(0,height+1):
        row = []
        for j in range(0,width+1):
            row.append(0)
        matrix.append(row)


    for i in range(0,height+1):
        for j in range(0,width+1):
            if (math.sqrt((i-radius)**2 + (j-radius)**2))  <= 0.5 + radius :                      

                if i == 0 or i == width:
                    matrix[i][j] = border_color
                elif (math.sqrt((i-radius)**2 + (j-radius)**2))  >= radius -0.3:
                        matrix[i][j] = border_color
                else:
                    matrix[i][j] = fill_color   
            else:
                matrix[i][j] = 0            

    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    # embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)

    embroider(draw_christmas_tree(4,border_color=1,fill_color=2),color_scheme)
