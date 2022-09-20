import com.qualcomm.robotcore.hardware.DcMotor


class Conveyer():
	def __init__(self):
		self.motor_conveyer = hardwareMap.dcMotor.get("motorConveyer")

	def activate(self, power=0.6):
		self.motor_conveyer.setPower(power)

	def deactivate(self):
		self.motor_conveyer.setPower(0)
