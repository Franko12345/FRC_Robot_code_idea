import com.qualcomm.robotcore.hardware.Controller
import time
import driverStation

class RobotCore():
	def __init__(self, chassiI, shooterI, conveyerI, waterPumpI, clawI, intakeI):
		self.chassiI = chassiI
		self.shooterI = shooterI
		self.conveyerI = conveyerI
		self.waterPumpI = waterPumpI
		self.clawI = clawI
		self.intakeI = intakeI
	
	def Start(self):
		self.intakeI.Activate()
		self.Autonomous()

	def Autonomous(self):
		autonomousTime = time.time()
		self.shooterI.shoot(conveyerI=self.conveyerI)
		
		self.chassiI.Curve(-150) 
		#virar o robõ do water tank para a water pump(como é no antihoraio tenho que botar negativo pra esse lado)

		self.chassiI.Straight(7.8)
		#andar 7.8 metros vai ficar 20cm de distância até a parede, pois estamos a 1m da parede do water tank

		self.chassiI.Curve(15)
		#ficar reto em relação a o water pump

		self.chassiI.Straight(0.1)
		#encostar na water pump

		self.waterPumpI.programWaterPump()
		#prorgamar water-pump

		while time.time()-autonomousTime <= 15:
			pass # esperar até acabar o tempo de autonomous

		self.TeleOps()

	def TeleOps(self):
		self.teleops = True
		self.Controller = hardwareMap.controller.get("controller1") #Input de controle exemplificado
		while self.teleops:

			#Buttons
			if driverStation.getInput('exit'): #botão para sair do teleops e desligar o robô
				self.teleops = False
			if self.Controller.getButtonRaw("X"): #shoot button
				self.shooterI.shoot(quantity=1, conveyerI = self.conveyerI)

			#Axis
			clawOutput = self.Controller.getAxisRaw("RIGHT_X") #controlador da garra

			self.clawI.motor_claw.setPower(clawOutput*0.7) #valor para calibrar

			driveSpeed = self.Controller.getAxisRaw('LEFT_Y') * 0.6 #0.3 e 0.6 pois é um valor para calibrar a curva e speed
			driveTurn = self.Controller.getAxisRaw('LEFT_X') * 0.3 #considerando as axis como valores entre -1 e 1

			driveLeft = driveSpeed + driveTurn
			driveRight = driveSpeed - driveTurn 

			self.chassiI.motorRight.setPower(driveRight)
			self.chassiI.motorLeft.setPower(driveLeft)
	
		self.End()
	
	def End(self):
		self.intakeI.Deactivate()