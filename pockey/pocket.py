x_size = input("X Dimension (Width): ")
y_size = input("Y Dimension (Height): ")
bit_diameter = input("Bit Diameter: ")
cross_over = input("Cross over percentage as decimal (Ex. 0.5): ")

x_size -= bit_diameter
y_size -= bit_diameter

string_buffer = ""
x_pos = 0
for raster_line in range(int((x_size-bit_diameter) / (bit_diameter * cross_over))):
    if(raster_line % 2 == 0):
        string_buffer += "G1 X"+str(x_pos)+'\n'
        string_buffer += "G1 Y"+str(y_size) + '\n'
    else:
        string_buffer += "G1 X"+str(x_pos) + '\n'
        string_buffer += "G1 Y0\n"

    x_pos += bit_diameter * cross_over

fl = open("out.gcode",'w')
fl.write(string_buffer)
fl.close()

print("Have a nice day!")
