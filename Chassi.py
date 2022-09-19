import com.qualcomm.robotcore.hardware.DcMotor
import com.qualcomm.robotcore.hardware.Sensor
import time
import math
import threading

#PID constants:
KP = 0.5 #constante proporcional do erro, caso usado não hípoteticamente necessita ser calibrado
KI = 2 #constante intergal da soma dos erros
KD = 0.1 # consatnte derivativa
IntegralLimit = 1


#Constantes de conversão:

TickToMeter = 1/4096 * math.pi * 0.14
#1 rotação a cada 4096 ticks * PI * diametro da roda 0.14m
#o motor nao conta com rotações, ele conta uma rotação a cada 4096 ticks

AngleToMeter = 1/360*(math.pi*2)
#eu que pensei nesse :) math.pi*2 pq o comprimento do robô é 1 o diametro da curva vai ser 2

class Chassi():
	def __init__(self):
		self.motorLeft1 = hardwareMap.dcMotor.get("motorLeft1")
		self.motorLeft2 = hardwareMap.dcMotor.get("motorLeft2")
		self.motorRight1 = hardwareMap.dcMotor.get("motorRight1")
		self.motorRight2 = hardwareMap.dcMotor.get("motorRight2")
		
		#PID needs:
		self.encoderLeft = hardwareMap.sensor.get("encoderMotorLeft")
		self.encoderLeft.reset()
		self.encoderRight = hardwareMap.sensor.get("encoderMotorRight")
		self.encoderRight.reset()
		self.errorSum = 0
		self.lastTime = time.time()
		self.lastError = 0

	def SetMotorGoal(self, motors:list, goal, encoder):
		sensor_pos = encoder.get() * TickToMeter # passar informação do encoder em ticks para metros
		while sensor_pos*TickToMeter < goal:
		
			sensor_pos = encoder.get() * TickToMeter	
			
			error = goal - sensor_pos #calculado distância atual até objetivo
			deltaTime = time.time() - self.lastTime 
			#usado para a correção de performance, pois nem 
			#toda a vez a função executara no mesmo tempo

			if abs(error) < IntegralLimit:
				#só vai adicionar o erro na soma se estiver dentro da range para adicionar
				#erros pequenos e não causar ocilação ou o aumento do erro
				self.errorSum += error * deltaTime

			errorRate = (error - self.lastError) / deltaTime #taxa de variação de erro

			outputSpeed = (KP * error) + (KI * errorSum) + (KD * errorRate) #apicação do PID

			for motor in motors:
				motor.setPower(outputSpeed)

			self.lastTime = time.time()
			self.lastError = error

		#desligar os motores quando chegar ao destino
		for motor in motors:
			motor.setPower(0)


	def Straight(self, goal):
		SetMotorGoal([self.motorLeft1, self.motorLeft2, self.motorRight1, self.motorRight2], goal, encoder=self.encoderLeft) 
		#indo reto então nao importa qual encoder escolher

	def Curve(self, angle):
		#sentido antí-horário
		threadRight = threading.Thread(target=SetMotorGoal, args=([self.motorRight1, self.motorRight2], (angle*AngleToMeter)/2, self.encoderRight))
		threadLeft = threading.Thread(target=SetMotorGoal, args=([self.motorLeft1, self.motorLeft2], -(angle*AngleToMeter)/2, self.encoderLeft))
		#curva necessia de encoder específico para cálculo PID
		#threads pois para os dois motores ser ativados ao mesmo tempo

		threadLeft.start()
		threadRight.start()
