arc_number = 8
radius = 1.5
output_buff = ""

bit_diameter = 3.175
half_bit = bit_diameter /2

from math import *

def downwards_arc(coord,depth,vec_count, offset):
    global output_buff
    inv_coord = [-coord[0], -coord[1]]
    output_buff += "G1 X"+str(inv_coord[0]+offset[0])+" Y"+str(inv_coord[1]+offset[1])+'\n'
    output_buff += "G1 F50"
    add_vec = ((coord[0]*2)/vec_count, (coord[1]*2)/vec_count)
    print("add_vec: "+str(add_vec))
    print("hello")
    for vec in range(vec_count+1):
        z = sqrt(depth**2 - ((abs((vec_count/2.)-vec) / (vec_count/2.)) * depth)**2) 
        print("z: "+str(z))
        output_buff += "G1 X"+str(round(inv_coord[0]+offset[0],4)) + " Y"+str(round(inv_coord[1]+offset[1],4))+" Z-"+str(round(z,4))+'\n'
        inv_coord[0] += add_vec[0]
        inv_coord[1] += add_vec[1]

        
RAD_MAX = pi*2

def gen_pock(center):
    rad_inc = pi/arc_number

    rad = 0
    for arc in range(arc_number):
        rad += rad_inc
        downwards_arc( (cos(rad)*radius, sin(rad)*radius), 1.5, 32, center)

def matrix():
    x_pos = half_bit+5
    y_pos = half_bit+5
    for columb in range(8):
        for row in range(8):
            output_buff += "g1 z3 f1000"
            gen_pock((x_pos, y_pos))
            x_pos += 10+bit_diameter

        y_pos += 10+bit_diameter
        x_pos = half_bit+5

def columb():
    x_pos = half_bit+5
    y_pos = half_bit+5
    for tile in range(8):
        gen_pock((x_pos,y_pos))
        x_pos += 10+bit_diameter

def cut_outs():
    global output_buff
    output_buff += "G1 Z-3.5 F50\n"
    output_buff += "G1 Y13.175 F30\n"
    x_pos = 0
    y_pos = 0
    for tile in range(4):
        
        output_buff += "G1 Z3 F500\n"
        output_buff += "G1 Y0\n"
        output_buff += "G1 X"+str(x_pos)+'\n'
        output_buff += "G1 Z-3.5 F50"
        output_buff += "G1 F30\n"
        output_buff += "G1 X"+str(x_pos+10+bit_diameter)+'\n'
        output_buff += "G1 Y13.175\n"
        output_buff += "G1 X"+str(x_pos)+" F30\n"

        x_pos += 10+bit_diameter


def rounded_cut_outs():
    global output_buff
    x_pos = 0
    y_pos = 0
    for tile in range(4):
        
        output_buff += "G1 Z3 F100\n"
        output_buff += "G1 Y13.175 X"+str(x_pos)+" F100\n"
        output_buff += "G1 Z-3.5 F30\n"
        output_buff += "G1 Y"+str(5.211+half_bit)+"\n"
        output_buff += "G3 X"+str(x_pos+5.211+half_bit)+" Y0 I"+str(5.211+half_bit)+'\n'
        output_buff += "G1 X"+str(x_pos+10+bit_diameter)+'\n'
        output_buff += "G1 Y13.175\n"
        output_buff += "G1 X"+str(x_pos)+"\n"

        x_pos += 10+bit_diameter


rounded_cut_outs()
#columb()
fl = open("out.gcode", 'w')
fl.write(output_buff)
fl.close()

print("Have a nice day!")
