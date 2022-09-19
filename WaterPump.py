import com.qualcomm.robotcore.hardware.DcMotor
import com.qualcomm.robotcore.hardware.Sensor
import time
import driverStation

def color(RGB):
	TRESHOLD_BLACK = 60
	TRESHOLD_WHITE = 195
	ColorFinal = []
	for color in RGB:
		if color <= TRESHOLD_BLACK:
			ColorFinal.append(0)
		elif color >= TRESHOLD_WHITE:
			ColorFinal.append(1)
	if ColorFinal == [0]*3:
		return 0
	elif ColorFinal == [1]*3:
		return 1
	return None		

class WaterPump():
	def __init__(self):
		self.motor_pump = hardwareMap.dcMotor.get("motorPump")
		self.color_sensor = hardwareMap.sensor.get("colorSensor")

		self.binary_code = list(driverStation.get("Binar_Input"))
	
	def programWaterPump(self):
		for binary_digit in self.binary_code:
			SelectedColor = color(self.color_sensor.getColor())

			self.motor_pump.setPower(0.4) 

			while SelectedColor == binary_digit: #para se ja começar na cor do digito mudar e depois procurar a certa
				SelectedColor = color(self.color_sensor.getColor())

			while SelectedColor != binary_digit: #procurar a cor certa após saír da que estáva
				SelectedColor = color(self.color_sensor.getColor())

			self.motor_pump.setPower(0) 
			time.sleep(1)

