function xx (num: number) {
    return convertToText(100 + num).substr(1, 2)
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    ds.DateTime(
    2021,
    4,
    26,
    7,
    17,
    50,
    0
    )
})
let zeit = ""
let datum = ""
let ds: DS1302.DS1302RTC = null
led.setBrightness(16)
basic.showIcon(IconNames.Heart)
ds = DS1302.create(DigitalPin.P13, DigitalPin.P14, DigitalPin.P15)
makerbit.clearLcd1602()
makerbit.setLcdBacklight(LcdBacklight.On)
basic.showIcon(IconNames.SmallHeart)
basic.forever(function () {
    datum = "" + xx(ds.getDay()) + "." + convertToText(xx(ds.getMonth())) + "." + convertToText(xx(ds.getYear()))
    zeit = "" + convertToText(xx(ds.getHour())) + ":" + convertToText(xx(ds.getMinute())) + ":" + convertToText(xx(ds.getSecond()))
    makerbit.showStringOnLcd1602(datum, makerbit.position1602(LcdPosition1602.Pos1), 16, TextOption.AlignCenter)
    makerbit.showStringOnLcd1602(zeit, makerbit.position1602(LcdPosition1602.Pos17), 16, TextOption.AlignCenter)
    basic.pause(500)
})
