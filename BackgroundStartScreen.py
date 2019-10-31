
start_x = 275
        start_y = 50
        #arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Tombstone", start_x, start_y, arcade.color.BLACK, 15, font_name='GARA')
arcade.draw_rectangle_filled(300,50 , 100, 50, arcade.color.WHITE)

arcade.draw_ellipse_filled(300, 300, 250, 150 arcade.color.ORANGE)
arcade.draw_rectangle_filled(300, 475, 40, 50, arcade.color.BROWN)


arcade.draw_triangle_filled(400,400,360,450, 320, 400 arcade.color.BLACK)

arcade.draw_triangle_filled(200,400, 240, 450,280, 400 arcade.color.BLACK)
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                        start_angle, end_angle, 10)

