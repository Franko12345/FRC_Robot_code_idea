// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.commands;

import frc.robot.subsystems.DriveSubsystem;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj2.command.CommandBase;

/** An example command that uses an example subsystem. */
public class DrivePIDControl extends CommandBase {
  private final DriveSubsystem driveTrain;
  private final double goal;
  
  private double errorSum;
  private double lastTime;
  private double lastError;
  private int side;

  public DrivePIDControl(DriveSubsystem driveTrain, double setPoint, int side) {
    this.driveTrain = driveTrain;
    this.goal = setPoint;
    this.side = side;
    // Use addRequirements() here to declare subsystem dependencies.
    addRequirements(this.driveTrain);
  }

  // Called when the command is initially scheduled.
  @Override
  public void initialize() {
    driveTrain.resetEncoders();
    this.errorSum = 0;
    this.lastTime = Timer.getFPGATimestamp();
    this.lastError = 0;
  }

  // Called every time the scheduler runs while the command is scheduled.
  private double sensor_pos;
  @Override
  public void execute() {
    sensor_pos = driveTrain.getEncoderMeters(side);
  }

  // Called once the command ends or is interrupted.
  @Override
  public void end(boolean interrupted) {}

  // Returns true when the command should end.
  @Override
  public boolean isFinished() {
    return false;
  }
}
