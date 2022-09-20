from RobotCore.py import *
from Chassi.py import *
from Shooter.py import *
from Conveyer.py import *
from WaterPump.py import *
from Claw.py import *
from Intake.py import *

def main():
	chassiInstance = Chassi()
	conveyerInstance = Conveyer()
	shooterInstance = Shooter()
	waterPumpInstance = WaterPump()
	clawInstance = Claw()

	Robot = RobotCore(chassiInstance, shooterInstance, conveyerInstance, waterPumpInstance, clawInstance)
	Robot.Start()

if __name__ == '__main__':
	main()
