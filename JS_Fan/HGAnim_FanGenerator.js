/* Fan Dimentions */
var BLADE_COUNT    = 8;
var BLADE_DIAMETER = 8;
var BLADE_LENGTH   = 100;
var CENTER_CIRCLE_RADIUS = 10;
var MOTOR_MOUNT_HOLE_DIAMETER = 3.8;

/* CNC and Spindle Values */
var BIT_DIAMETER = 3.175;
var SAFE_Z       = 2
var CUT_DEPTH    = -3.175;
var CUT_FEEDRATE = 200;
var PLUNGE_RATE  = 50;
var BLADE_RASTER_RATE = 200;
var RASTER_STEP_SIZE  = 0.1;


var BIT_RADIUS;
var FULL_BLADE_SECTION_ANGLE;

var FULL_ROT = Math.pi * 2;


var Global_GCode_Buffer = new StringBuffer(); // gcode file is built in this string
function GCode(){             // function for appending to buffer
	var gcode_command = arguments[0];
	Global_GCode_Buffer.append(gcode_command);
	for(var i=1;i<arguments.length;i+=2){
		Global_GCode_Buffer.append(' '+ arguments[i] + arguments[i+1])
	}
	Global_GCode_Buffer.append("\n");
}
function INIT(){
	BIT_RADIUS = BIT_DIAMETER / 2;
	FULL_BLADE_SECTION = FULL_ROT / BLADE_COUNT;
    
    Generate_GCode();
}
function Generate_Profile(){
	var half_blade_diameter = BLADE_DIAMETER + BIT_DIAMETER / 2;
	var center_circle_radius = CENTER_CIRCLE_RADIUS + BIT_RADIUS;
	var blade_radius = Math.arccos(half_blade_diameter/center_circle_radius) * 2;
	var outer_section_angle = FULL_BLADE_SECTION_ANGLE - blade_radius;

	for(var blade=0;blade<BLADE_COUNT;blade++){
		//var point_one = 
	}
}
function Write_GCode(){
	console.log(Global_GCode_Buffer.toString());
}
function Left_Bit_Comp(x){ return x+BIT_RADIUS; } //componsate for bit radius on a left cut
function Right_Bit_Comp(x){ return x-BIT_RADIUS; } //componsate for bit radius on a right cut
function Upper_Bit_Comp(y){ return y-BIT_RADIUS; } //componsate for bit radius on a upper cut
function Lower_Bit_Comp(y){ return y+BIT_RADIUS; } //componsate for bit radius on a lower cut

function Move(){
	GCode.apply(null,
                ['G0'].concat(Array.from(arguments)) //apply G0 to beginning
               );
}
function Drill(){
	GCode.apply(null,
                [].concat(Array.prototype.unshift.call(arguments,'G1')) //apply G1 to beginning
               );
}
function Set_FeedRate(feedrate){
	GCode("G1", "F", feedrate);
}
function Plunge(){
	Set_FeedRate(PLUNGE_RATE);
	Move("Z", CUT_DEPTH);
	Set_FeedRate(CUT_FEEDRATE);
}


function Generate_GCode()
{
    Move("Z", SAFE_Z);
	Generate_Motor_Mount_Hole();
	Write_GCode();
}

    
function Generate_Motor_Mount_Hole(){
	var left = Left_Bit_Comp(-CENTER_CIRCLE_RADIUS);
	var right = Right_Bit_Comp(CENTER_CIRCLE_RADIUS);
	var upper = Upper_Bit_Comp(CENTER_CIRCLE_RADIUS);
	var lower = Lower_Bit_Comp(-CENTER_CIRCLE_RADIUS);
	Move(
			"X", left,
		   	"Y", 0
		);

	Plunge();
	GCode("G2",
			"X", 0,
			"Y", upper,
			"I", right,
			"J", 0
			);

	GCode("G2",
			"X", right, 
			"Y", 0,
			"I", 0,
			"J", lower
			);

	GCode("G2",
			"X", 0,
			"Y", lower,
			"I", left,
			"J", 0
		 );
	GCode("G2",
			"X", left,
			"Y", 0,
			"I", 0,
			"J", upper
		 );
}




INIT();
