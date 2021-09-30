def on_button_pressed_a():
    global szam
    szam += 1
    basic.show_number(szam)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if szam == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
    if szam == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        . # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . # . .
                        . # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . # .
                        # . # . .
                        . # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . # .
                        # . # . .
                        . # . . .
        """)
    if szam == 3:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . .
                        # . . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        # # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . # # # .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
                        . . . # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . #
                        . . . . #
                        . . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . . #
                        . . . . #
                        . . . . .
        """)
        basic.show_leds("""
            . . . . #
                        . . . . #
                        . . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . # #
                        . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . # # # .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

szam = 0
szam = 0

def on_forever():
    global szam
    if szam == 4:
        szam = 1
        basic.show_number(szam)
basic.forever(on_forever)
