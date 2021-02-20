gcode = ""
bit_diameter = 3.175
material_depth = 3.175
raster_crossover = 0.5
Z_safe_depth=2#-78
top_cut_depth=0#-80
feed_rate=50
Z_feed_rate = 20
blade_diameter = 5

half_dia = (bit_diameter/2)
def blade_one():
	global gcode
	top_y = 5+16+16+16 + half_dia
	bottom_y = 5+16+16+half_dia
	left_x = 5+16+8-2.5+half_dia
	right_x = 5+16+8+2.5+half_dia
	plunge_depth = top_cut_depth-material_depth
	
	gcode += "G0 X{} Y{} Z{}\n".format(left_x, top_y, Z_safe_depth) #move above beginning spot
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate) #lower to begin cut
	gcode += "G1 F{}\n".format(feed_rate)

	current_y = top_y
	current_x = left_x
	while(current_y>(bottom_y+half_dia)):
		print("Hello!")
		if(current_x == left_x): #downward plunge
			current_x = right_x
			gcode += "G1 X{} Z{}\n".format(right_x, plunge_depth)
		elif(current_x == right_x): #plunge upwards
			current_x = left_x
			gcode += "G1 X{} Z{}\n".format(left_x, top_cut_depth)
		else:
			print ("Something went wrong while generating gcode error id: 0")
			exit(1)

		current_y -= bit_diameter * raster_crossover
		gcode += "G1 Y{}\n".format(current_y)
		

	if(current_x == left_x): #downward plunge
		current_x = right_x
		gcode += "G1 X{} Z{}\n".format(right_x, plunge_depth)
	elif(current_x == right_x): #plunge upwards
		current_x = left_x
		gcode += "G1 X{} Z{}\n".format(left_x, top_cut_depth)


	gcode += "G1 Z{}\n".format(Z_safe_depth)
	gcode += "G0 X{} Y{}\n".format(left_x, bottom_y)
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate)
	gcode += "G1 F{}\n".format(feed_rate)
	gcode += "G1 X{} Z{}\n".format(right_x, plunge_depth)
	gcode += "G1 Z{}\n".format(Z_safe_depth)

def blade_two():
	global gcode
	top_y = 5-half_dia
	bottom_y = 5+16
	left_x = 5+16+8-2.5-half_dia
	right_x = 5+16+8+2.5-half_dia
	plunge_depth = top_cut_depth-material_depth
	
	gcode += "G0 X{} Y{} Z{}\n".format(right_x, top_y, Z_safe_depth) #move above beginning spot
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate) #lower to begin cut
	gcode += "G1 F{}\n".format(feed_rate)

	current_y = top_y
	current_x = right_x
	while(current_y<(bottom_y-bit_diameter)):
		if(current_x == right_x): #downward plunge
			current_x = left_x
			gcode += "G1 X{} Z{}\n".format(left_x, plunge_depth)
		elif(current_x == left_x): #plunge upwards
			current_x = right_x
			gcode += "G1 X{} Z{}\n".format(right_x, top_cut_depth)
		else:
			print ("Something went wrong while generating gcode error id: 0")
			exit(1)

		current_y += bit_diameter * raster_crossover
		gcode += "G1 Y{}\n".format(current_y)
		

	if(current_x == right_x): #downward plunge
		current_x = left_x
		gcode += "G1 X{} Z{}\n".format(left_x, plunge_depth)
	elif(current_x == left_x): #plunge upwards
		current_x = right_x
		gcode += "G1 X{} Z{}\n".format(right_x, top_cut_depth)

	gcode += "G1 Z{}\n".format(Z_safe_depth)
	gcode += "G0 X{} Y{}\n".format(right_x, top_y)
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate)
	gcode += "G1 F{}\n".format(feed_rate)
	gcode += "G1 X{} Z{}\n".format(left_x, plunge_depth)
	gcode += "G1 Z{}\n".format(Z_safe_depth)

def blade_three():
	global gcode
	top_y = 5+16+8+2.5
	bottom_y = 5+16+8-2.5
	left_x = 5
	right_x = 5+16
	plunge_depth = top_cut_depth-material_depth

	gcode += "G0 X{} Y{} Z{}\n".format(left_x, bottom_y+half_dia, Z_safe_depth) #move above beginning spot
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate) #lower to begin cut
	gcode += "G1 F{}\n".format(feed_rate)

	bottom_bounds = bottom_y+half_dia
	top_bounds = top_y+half_dia
	current_y = bottom_bounds
	current_x = left_x
	while(current_x<(right_x-bit_diameter)):
		if(current_y == bottom_bounds): #downward plunge
			current_y = top_bounds
			gcode += "G1 Y{} Z{}\n".format(top_bounds, plunge_depth)
		elif(current_y == top_bounds): #plunge upwards
			current_y = bottom_bounds
			gcode += "G1 Y{} Z{}\n".format(bottom_bounds, top_cut_depth)
		else:
			print ("Something went wrong while generating gcode error id: 0")
			exit(1)

		current_x += bit_diameter * raster_crossover
		gcode += "G1 X{}\n".format(current_x)

	if(current_y == bottom_bounds): #downward plunge
		current_y = top_bounds
		gcode += "G1 Y{} Z{}\n".format(top_bounds, plunge_depth)
	elif(current_x == top_bounds): #plunge upwards
		current_y = bottom_bounds
		gcode += "G1 Y{} Z{}\n".format(bottom_bounds, top_cut_depth)

	gcode += "G1 Z{}\n".format(Z_safe_depth)
	gcode += "G0 X{} Y{}\n".format(right_x-half_dia, bottom_bounds)
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate)
	gcode += "G1 F{}\n".format(feed_rate)
	gcode += "G1 Y{} Z{}\n".format(top_bounds, plunge_depth)
	gcode += "G1 Z{}\n".format(Z_safe_depth)

def blade_four():
	global gcode
	top_y = 5+16+8+2.5
	bottom_y = 5+16+8-2.5
	left_x = 5+16+16
	right_x = left_x+16
	plunge_depth = top_cut_depth-material_depth

	gcode += "G0 X{} Y{} Z{}\n".format(left_x+half_dia, top_y-half_dia, Z_safe_depth) #move above beginning spot
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate) #lower to begin cut
	gcode += "G1 F{}\n".format(feed_rate)

	bottom_bounds = bottom_y-half_dia
	top_bounds = top_y-half_dia
	current_y = top_bounds
	current_x = left_x
	while(current_x<(right_x-half_dia)):
		if(current_y == top_bounds): #downward plunge
			current_y = bottom_bounds
			gcode += "G1 Y{} Z{}\n".format(bottom_bounds, plunge_depth)
		elif(current_y == bottom_bounds): #plunge upwards
			current_y = top_bounds
			gcode += "G1 Y{} Z{}\n".format(top_bounds, top_cut_depth)
		else:
			print ("Something went wrong while generating gcode error id: 0")
			exit(1)

		current_x += bit_diameter * raster_crossover
		gcode += "G1 X{}\n".format(current_x)

	if(current_y == top_bounds): #downward plunge
		current_y = bottom_bounds
		gcode += "G1 Y{} Z{}\n".format(bottom_bounds, plunge_depth)
	elif(current_y == bottom_bounds): #plunge upwards
		current_y = top_bounds_bounds
		gcode += "G1 Y{} Z{}\n".format(top_bounds, top_cut_depth)

	gcode += "G1 Z{}\n".format(Z_safe_depth)
	gcode += "G0 X{} Y{}\n".format(right_x, top_bounds)
	gcode += "G1 Z{} F{}\n".format(top_cut_depth, Z_feed_rate)
	gcode += "G1 F{}\n".format(feed_rate)
	gcode += "G1 Y{} Z{}\n".format(bottom_bounds, plunge_depth)
	gcode += "G1 Z{}\n".format(Z_safe_depth)


	
	
	
	
	


def gen_fan_engraving(): 
	blade_one()
	blade_two()
	blade_three()
	blade_four()


gen_fan_engraving();

fl = open("output.gcode", "w")
fl.write(gcode)
fl.close()


'''import pygame as pg
build_volume = (450,390)
background = (0,0,0)
screen = pg.display.set_mode(build_volume)
'''
