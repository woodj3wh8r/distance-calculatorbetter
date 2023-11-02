controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    place_holder += 1
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    place_holder += -10
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    textSprite = textsprite.create("" + distf + " pixels")
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    place_holder += -1
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    place_holder += 10
})
function on_a_pressed () {
    if (cordstep == 1) {
        x1 = place_holder
        place_holder = 0
        cordstep += 1
    } else if (cordstep == 2) {
        cord_type = "y" + ""
        y1 = place_holder
        place_holder = 0
        cordstep += 1
    } else if (cordstep == 3) {
        cord_type = "x" + ""
        cord_set += 1
        x2 = place_holder
        place_holder = 0
        cordstep += 1
    } else if (cordstep == 4) {
        cord_type = "y" + ""
        y2 = place_holder
        place_holder = 0
        cordstep += 1
    } else {
    	
    }
}
let diste = 0
let distd = 0
let distc = 0
let distb = 0
let current_phase = ""
let y2 = 0
let x2 = 0
let y1 = 0
let x1 = 0
let distf = 0
let textSprite: TextSprite = null
let cordstep = 0
let cord_type = ""
let place_holder = 0
let dist = 0
controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
place_holder = 0
cord_type = "x" + ""
let cord_set = 1
cordstep = 1
let numbers = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
let n2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
let answer = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
n2.setPosition(68, 97)
answer.setPosition(74, 99)
controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
// def on_forever():
// n2.say_text("" + str(x1) + "__" + ("" + str(y1)) + "__" + ("" + str(x2) + "__" + ("" + str(y2))))
// forever(on_forever)
forever(function () {
    current_phase = "" + cord_type + ("" + cord_set) + ":" + ("" + place_holder)
    numbers.sayText(current_phase)
})
forever(function () {
    let dista = 0
    distb = y2 - y1
    distc = Math.imul(dista, 2)
    distd = distb * distb
    diste = distc + distd
    distf = Math.sqrt(diste)
})
