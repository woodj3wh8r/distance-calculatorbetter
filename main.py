def on_up_pressed():
    global place_holder
    place_holder += 1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    global place_holder
    place_holder += -10
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_b_pressed():
    global textSprite
    textSprite = textsprite.create("" + str(distf) + " pixels")
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_down_pressed():
    global place_holder
    place_holder += -1
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_a_pressed():
    global x1, place_holder, cordstep, cord_type, y1, cord_set, x2, y2
    if cordstep == 1:
        x1 = place_holder
        place_holder = 0
        cordstep += 1
    elif cordstep == 2:
        cord_type = "y" + ""
        y1 = place_holder
        place_holder = 0
        cordstep += 1
    elif cordstep == 3:
        cord_type = "x" + ""
        cord_set += 1
        x2 = place_holder
        place_holder = 0
        cordstep += 1
    elif cordstep == 4:
        cord_type = "y" + ""
        y2 = place_holder
        place_holder = 0
        cordstep += 1
    else:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_pressed():
    global place_holder
    place_holder += 10
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

diste = 0
distd = 0
distc = 0
distb = 0
current_phase = ""
y2 = 0
x2 = 0
y1 = 0
x1 = 0
distf = 0
textSprite: TextSprite = None
cordstep = 0
cord_type = ""
place_holder = 0
dist = 0
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
place_holder = 0
cord_type = "x" + ""
cord_set = 1
cordstep = 1
numbers = sprites.create(img("""
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
    """),
    SpriteKind.player)
n2 = sprites.create(img("""
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
    """),
    SpriteKind.player)
answer = sprites.create(img("""
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
    """),
    SpriteKind.player)
n2.set_position(68, 97)
answer.set_position(74, 99)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
# def on_forever():
# n2.say_text("" + str(x1) + "__" + ("" + str(y1)) + "__" + ("" + str(x2) + "__" + ("" + str(y2))))
# forever(on_forever)

def on_forever():
    global current_phase
    current_phase = "" + cord_type + ("" + str(cord_set)) + ":" + ("" + str(place_holder))
    numbers.say_text(current_phase)
forever(on_forever)

def on_forever2():
    global distb, distc, distd, diste, distf
    dista = 0
    distb = y2 - y1
    distc = Math.imul(dista, 2)
    distd = distb * distb
    diste = distc + distd
    distf = Math.sqrt(diste)
forever(on_forever2)
