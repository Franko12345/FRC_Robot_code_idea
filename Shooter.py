import com.qualcomm.robotcore.hardware.DcMotor
import com.qualcomm.robotcore.hardware.Sensor

class Shooter():
	def __init__(self, Conveyer):
		self.motor_shooter = hardwareMap.dcMotor.get("motorShooter")
		self.sensor_shooter = hardwareMap.sensor.get("sensorShooter")
		self.Conveyer = Conveyer

	def shoot(self, power=0.6, quantity=5, conveyerI):
		conveyerI.activate(power)	
		self.motor_shooter.setPower(power)

		for x in range(quantity):
			while not self.sensor_shooter.is_pressed(): #espera até o sensor ter uma bolinha
				pass
			while self.sensor_shooter.is_pressed(): #espera até o sensor não ter mais uma bolinha então ele atirou
				pass			
			#repita 5 vezes para ver se atirou todas
	
		conveyerI.deactivate()	
		self.motor_shooter.setPower(0)
		return True

