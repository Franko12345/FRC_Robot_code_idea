// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.subsystems;

import edu.wpi.first.wpilibj.Encoder;
import edu.wpi.first.wpilibj.Spark;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class DriveSubsystem extends SubsystemBase {
  private final Spark driveLeftMotor = new Spark(0);
  private final Spark driveRightMotor = new Spark(1);
  private final Encoder encoderLeft = new Encoder(0,1);
  private final Encoder encoderRight = new Encoder(2,3);
  //PID constants:
  private final float KP = 0.5f; //constante proporcional do erro, caso usado não hípoteticamente necessita ser calibrado
  private final float KI = 2.0f; //constante intergal da soma dos erros
  private final float KD = 0.1f; // consatnte derivativa
  private final float IntegralLimit = 1;

  //Constantes de conversão:

  private final double TickToMeter = 1/4096 * Math.PI * 0.14;
  //1 rotação a cada 4096 ticks * PI * diametro da roda 0.14m
  //o motor nao conta com rotações, ele conta uma rotação a cada 4096 ticks

  private final double AngleToMeter = 1/360*(Math.PI*2);
  //eu que pensei nesse :) math.pi*2 pq o comprimento do robô é 1 o diametro da curva vai ser 2
  public double getEncoderMeters(int n){
    if (n==0){
      return encoderLeft.get() * TickToMeter;
    }else if(n==1){
      return encoderRight.get() * TickToMeter;
    }
  }
  public double getMeterByAngle(double angle){
    return angle*AngleToMeter;
  }
  public void resetEncoders(){
    encoderLeft.reset();
    encoderRight.reset();
  }

  /** Creates a new ExampleSubsystem. */
  public DriveSubsystem() {
    driveLeftMotor.setInverted(false);
    driveLeftMotor.setInverted(true);
    encoderLeft.setReverseDirection(false);
    encoderRight.setReverseDirection(true);

  }

  @Override
  public void periodic() {
    // This method will be called once per scheduler run
  }

  public void setMotors(double leftSpeed, double rightSpeed){
    driveLeftMotor.set(leftSpeed);
    driveLeftMotor.set(-rightSpeed);
  }


  @Override
  public void simulationPeriodic() {
    // This method will be called once per scheduler run during simulation
  }
}
