def right(option: number):
    if option == 0:
        goRight(motor_speed)
    elif option == 1:
        armRight()
    elif option == 2:
        palmRight()
    else:
        pass
def armRight():
    global arm_moveLR
    arm_moveLR = 0 - servo_speed
def armParking():
    global arm_positionLR, arm_positionUD, palm_positionLR, palm_positionOC
    palmStop()
    armStop()
    arm_positionLR = 100
    arm_positionUD = arm_limitD
    palm_positionLR = 130
    palm_positionOC = 50
def armUp():
    global arm_moveUD
    arm_moveUD = servo_speed
def movePositions():
    global arm_moveUD, arm_positionUD, arm_moveLR, arm_positionLR, palm_moveOC, palm_positionOC, palm_moveLR, palm_positionLR
    if arm_positionUD < arm_limitD:
        arm_moveUD = 0
        arm_positionUD = arm_limitD
    elif arm_positionUD > arm_limitU:
        arm_moveUD = 0
        arm_positionUD = arm_limitU
    else:
        arm_positionUD += arm_moveUD
    if arm_positionLR < arm_limitR:
        arm_moveLR = 0
        arm_positionLR = arm_limitR
    elif arm_positionLR > arm_limitL:
        arm_moveLR = 0
        arm_positionLR = arm_limitL
    else:
        arm_positionLR += arm_moveLR
    if palm_positionOC < palm_limitC:
        palm_moveOC = 0
        palm_positionOC = palm_limitC
    elif palm_positionOC > palm_limitO:
        palm_moveOC = 0
        palm_positionOC = palm_limitO
    else:
        palm_positionOC += palm_moveOC
    if palm_positionLR < palm_limitL:
        palm_moveLR = 0
        palm_positionLR = palm_limitL
    elif palm_positionLR > palm_limitR:
        palm_moveLR = 0
        palm_positionLR = palm_limitR
    else:
        palm_positionLR += palm_moveLR
def palmRight():
    global palm_moveLR
    palm_moveLR = servo_speed
def goBackward(speed: number):
    robotbit.motor_run_dual(robotbit.Motors.M1A, speed, robotbit.Motors.M2A, speed)
def goForward(speed: number):
    goBackward(0 - speed)
# pushed button UP
def up(option: number):
    if option == 0:
        goForward(motor_speed)
    elif option == 1:
        armDown()
    elif option == 2:
        palmClose()
    else:
        pass
def left(option: number):
    if option == 0:
        goLeft(motor_speed)
    elif option == 1:
        armLeft()
    elif option == 2:
        palmLeft()
    else:
        pass

def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def stop(option: number):
    goStop()
    armStop()
    palmStop()

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def goStop():
    robotbit.motor_stop_all()
def armLeft():
    global arm_moveLR
    arm_moveLR = servo_speed
def palmClose():
    global palm_moveOC
    palm_moveOC = 0 - servo_speed
def armDown():
    global arm_moveUD
    arm_moveUD = 0 - servo_speed
def goRight(speed: number):
    goLeft(0 - speed)
def goLeft(speed: number):
    robotbit.motor_run_dual(robotbit.Motors.M1A, speed, robotbit.Motors.M2A, 0 - speed)
def armStop():
    global arm_moveUD, arm_moveLR
    arm_moveUD = 0
    arm_moveLR = 0
def palmOpen():
    global palm_moveOC
    palm_moveOC = servo_speed
def down(option: number):
    if option == 0:
        goBackward(motor_speed)
    elif option == 1:
        armUp()
    elif option == 2:
        palmOpen()
    else:
        pass

def on_mes_dpad_controller_id_microbit_evt():
    global control2
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_UP or (control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_UP or (control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_UP or control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_UP)):
        control2 = 0
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        control2 = 1
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        control2 = 2
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        armParking()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        pass
    else:
        pass
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_UP or (control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_UP or (control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_UP or control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_UP)):
        stop(control2)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        up(control2)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        down(control2)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        left(control2)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        right(control2)
    else:
        pass
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

def palmLeft():
    global palm_moveLR
    palm_moveLR = 0 - servo_speed
def palmStop():
    global palm_moveOC, palm_moveLR
    palm_moveOC = 0
    palm_moveLR = 0
def setServos():
    robotbit.servo(robotbit.Servos.S1, arm_positionLR)
    robotbit.servo(robotbit.Servos.S2, arm_positionUD)
    robotbit.servo(robotbit.Servos.S3, palm_positionLR)
    robotbit.servo(robotbit.Servos.S4, palm_positionOC)
control2 = 0
palm_moveLR = 0
palm_moveOC = 0
arm_moveUD = 0
palm_positionOC = 0
palm_positionLR = 0
arm_positionUD = 0
arm_positionLR = 0
arm_moveLR = 0
palm_limitR = 0
palm_limitL = 0
palm_limitC = 0
palm_limitO = 0
arm_limitR = 0
arm_limitL = 0
arm_limitD = 0
arm_limitU = 0
servo_speed = 0
motor_speed = 0
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

def on_forever():
    movePositions()
    setServos()
basic.forever(on_forever)
