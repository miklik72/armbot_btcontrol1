function right (option: number) {
    if (option == 0) {
        goRight(motor_speed)
    } else if (option == 1) {
        armRight()
    } else if (option == 2) {
        palmRight()
    } else {
    	
    }
}
function armRight () {
    arm_moveLR = 0 - servo_speed
}
function armParking () {
    palmStop()
    armStop()
    arm_positionLR = 100
    arm_positionUD = arm_limitD
    palm_positionLR = 130
    palm_positionOC = 50
}
function armUp () {
    arm_moveUD = servo_speed
}
function movePositions () {
    if (arm_positionUD < arm_limitD) {
        arm_moveUD = 0
        arm_positionUD = arm_limitD
    } else if (arm_positionUD > arm_limitU) {
        arm_moveUD = 0
        arm_positionUD = arm_limitU
    } else {
        arm_positionUD += arm_moveUD
    }
    if (arm_positionLR < arm_limitR) {
        arm_moveLR = 0
        arm_positionLR = arm_limitR
    } else if (arm_positionLR > arm_limitL) {
        arm_moveLR = 0
        arm_positionLR = arm_limitL
    } else {
        arm_positionLR += arm_moveLR
    }
    if (palm_positionOC < palm_limitC) {
        palm_moveOC = 0
        palm_positionOC = palm_limitC
    } else if (palm_positionOC > palm_limitO) {
        palm_moveOC = 0
        palm_positionOC = palm_limitO
    } else {
        palm_positionOC += palm_moveOC
    }
    if (palm_positionLR < palm_limitL) {
        palm_moveLR = 0
        palm_positionLR = palm_limitL
    } else if (palm_positionLR > palm_limitR) {
        palm_moveLR = 0
        palm_positionLR = palm_limitR
    } else {
        palm_positionLR += palm_moveLR
    }
}
function palmRight () {
    palm_moveLR = servo_speed
}
function goBackward (speed: number) {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    speed,
    robotbit.Motors.M2A,
    speed
    )
}
function goForward (speed: number) {
    goBackward(0 - speed)
}
// pushed button UP
function up (option: number) {
    if (option == 0) {
        goForward(motor_speed)
    } else if (option == 1) {
        armDown()
    } else if (option == 2) {
        palmClose()
    } else {
    	
    }
}
function left (option: number) {
    if (option == 0) {
        goLeft(motor_speed)
    } else if (option == 1) {
        armLeft()
    } else if (option == 2) {
        palmLeft()
    } else {
    	
    }
}
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
function stop (option: number) {
    goStop()
    armStop()
    palmStop()
}
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
function goStop () {
    robotbit.MotorStopAll()
}
function armLeft () {
    arm_moveLR = servo_speed
}
function palmClose () {
    palm_moveOC = 0 - servo_speed
}
function armDown () {
    arm_moveUD = 0 - servo_speed
}
function goRight (speed: number) {
    goLeft(0 - speed)
}
function goLeft (speed: number) {
    robotbit.MotorRunDual(
    robotbit.Motors.M1A,
    speed,
    robotbit.Motors.M2A,
    0 - speed
    )
}
function armStop () {
    arm_moveUD = 0
    arm_moveLR = 0
}
function palmOpen () {
    palm_moveOC = servo_speed
}
function down (option: number) {
    if (option == 0) {
        goBackward(motor_speed)
    } else if (option == 1) {
        armUp()
    } else if (option == 2) {
        palmOpen()
    } else {
    	
    }
}
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_UP || (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_UP || (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_UP || control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_UP))) {
        control2 = 0
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN) {
        control2 = 1
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_DOWN) {
        control2 = 2
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN) {
        armParking()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN) {
    	
    } else {
    	
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_UP || (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_UP || (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_UP || control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_UP))) {
        stop(control2)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        up(control2)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        down(control2)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        left(control2)
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        right(control2)
    } else {
    	
    }
})
function palmLeft () {
    palm_moveLR = 0 - servo_speed
}
function palmStop () {
    palm_moveOC = 0
    palm_moveLR = 0
}
function setServos () {
    robotbit.Servo(robotbit.Servos.S1, arm_positionLR)
    robotbit.Servo(robotbit.Servos.S2, arm_positionUD)
    robotbit.Servo(robotbit.Servos.S3, palm_positionLR)
    robotbit.Servo(robotbit.Servos.S4, palm_positionOC)
}
let control2 = 0
let palm_moveLR = 0
let palm_moveOC = 0
let arm_moveUD = 0
let palm_positionOC = 0
let palm_positionLR = 0
let arm_positionUD = 0
let arm_positionLR = 0
let arm_moveLR = 0
let palm_limitR = 0
let palm_limitL = 0
let palm_limitC = 0
let palm_limitO = 0
let arm_limitR = 0
let arm_limitL = 0
let arm_limitD = 0
let arm_limitU = 0
let servo_speed = 0
let motor_speed = 0
motor_speed = 100
servo_speed = 2
arm_limitU = 135
arm_limitD = 0
arm_limitL = 220
arm_limitR = 0
palm_limitO = 150
palm_limitC = 30
palm_limitL = 0
palm_limitR = 250
armParking()
setServos()
basic.forever(function () {
    movePositions()
    setServos()
})
