angle = 90

def on_button_pressed_a():
    global angle
    angle = Math.min(180,angle+45)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global angle
    angle = Math.max(0,angle-45)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pins.servo_write_pin(AnalogPin.P0, angle)
    basic.show_number(angle / 45)
basic.forever(on_forever)
