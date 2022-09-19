import com.qualcomm.robotcore.hardware.DcMotor

class Claw():
	def __init__(self):
		self.motor_claw = hardwareMap.dcMotor.get("motorclaw")