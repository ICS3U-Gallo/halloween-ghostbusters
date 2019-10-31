
start_x = 320
        start_y = 140
        #arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Tombstone", start_x, start_y, arcade.color.BLACK, 15, font_name='GARA')
arcade.draw_rectangle_filled(400,130 , 300, 170, arcade.color.WHITE)

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.ORANGE)

arcade.draw_triangle_filled(400,400,380,450, 360, 400 arcade.color.BLACK)

arcade.draw_triangle_filled(200,400, 220, 450,240, 400 arcade.color.BLACK)
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                        start_angle, end_angle, 10)
