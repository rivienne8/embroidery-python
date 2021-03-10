import embroidery as emb
color_scheme = {0: '   ', 1: ' 1 ', 2: ' . '}

# print(emb.draw_rectangle(6,7))
emb.embroider(emb.draw_rectangle(7,9,border_color = 2,fill_color = 1, border_width = 3),color_scheme)

# print(emb.draw_triangle(5))
emb.embroider(emb.draw_triangle(7,border_color = 2,fill_color = 1, border_width = 0),color_scheme)

# print(emb.draw_christmas_tree(2))
emb.embroider(emb.draw_christmas_tree(4,border_color=1,fill_color=2),color_scheme)

# emb.draw_circle(20)
emb.embroider(emb.draw_circle(15,1,2),color_scheme)

