zp = 0
yp = 0
xp = 0
s = 0
z = 0
y = 0
x = 0
basic.show_icon(IconNames.NO)
basic.show_icon(IconNames.YES)

def on_forever():
    global x, y, z, s, xp, yp, zp
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    s = input.acceleration(Dimension.STRENGTH)
    xp = Math.map(x, -1023, 1023, 0, 4)
    yp = Math.map(y, -1023, 1023, 0, 4)
    zp = Math.map(z, -1023, 1023, 0, 4)
    basic.clear_screen()
    led.plot_brightness(xp, 0, 128)
    led.plot_brightness(yp, 2, 64)
    led.plot_brightness(zp, 4, 16)
    makerbit.clear_lcd1602()
    makerbit.show_string_on_lcd1602(convert_to_text(x),
        makerbit.position1602(LcdPosition1602.POS1),
        8)
    makerbit.show_string_on_lcd1602(convert_to_text(y),
        makerbit.position1602(LcdPosition1602.POS9),
        8)
    makerbit.show_string_on_lcd1602(convert_to_text(z),
        makerbit.position1602(LcdPosition1602.POS17),
        8)
    makerbit.show_string_on_lcd1602(convert_to_text(s),
        makerbit.position1602(LcdPosition1602.POS25),
        8)
    basic.pause(100)
basic.forever(on_forever)
