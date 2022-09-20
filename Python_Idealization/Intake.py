import com.qualcomm.robotcore.hardware.DcMotor

class Intake():
	def __init__(self):
		self.motor_intake1 = hardwareMap.dcMotor.get("motorIntake1")
		self.motor_intake2 = hardwareMap.dcMotor.get("motorIntake2")
	
	def Activate(self, power=0.6):
		self.motor_intake1.setPower(power)
		self.motor_intake2.setPower(power)

	def Deactivate(self):
		self.motor_intake1.setPower(0)
		self.motor_intake2.setPower(0)