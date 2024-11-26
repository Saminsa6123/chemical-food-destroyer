def on_a_pressed():
    global pill
    pill = sprites.create_projectile_from_sprite(assets.image("""
        pill
    """), ship, 0, -140)
    pill.start_effect(effects.cool_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    scene.camera_shake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.start_effect(effects.fire, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

pill: Sprite = None
ship: Sprite = None
chemical_foods = [img("""
        . . . . c c c b b b b b . . . . 
            . . c c b 4 4 4 4 4 4 b b b . . 
            . c c 4 4 4 4 4 5 4 4 4 4 b c . 
            . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
            e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
            e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
            e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
            . e b 4 4 4 4 4 5 4 4 4 4 b e . 
            8 7 e e b 4 4 4 4 4 4 b e e 6 8 
            8 7 2 e e e e e e e e e e 2 7 8 
            e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
            e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
            e b e 8 8 c c 8 8 c c c 8 e b e 
            e e b e c c e e e e e c e b e e 
            . e e b b 4 4 4 4 4 4 4 4 e e . 
            . . . c c c c c e e e e e . . .
    """),
    img("""
        . . 2 2 b b b b b . . . . . . . 
            . 2 b 4 4 4 4 4 4 b . . . . . . 
            2 2 4 4 4 4 d d 4 4 b . . . . . 
            2 b 4 4 4 4 4 4 d 4 b . . . . . 
            2 b 4 4 4 4 4 4 4 d 4 b . . . . 
            2 b 4 4 4 4 4 4 4 4 4 b . . . . 
            2 b 4 4 4 4 4 4 4 4 4 e . . . . 
            2 2 b 4 4 4 4 4 4 4 b e . . . . 
            . 2 b b b 4 4 4 b b b e . . . . 
            . . e b b b b b b b e e . . . . 
            . . . e e b 4 4 b e e e b . . . 
            . . . . . e e e e e e b d b b . 
            . . . . . . . . . . . b 1 1 3 b 
            . . . . . . . . . . . c 1 d d b 
            . . . . . . . . . . . c 1 b c . 
            . . . . . . . . . . . . c c . .
    """),
    img("""
        . . . . . . 2 2 2 2 . . . . . . 
            . . . . 2 2 3 3 3 3 2 e . . . . 
            . . . 2 3 d 1 1 d d 3 2 e . . . 
            . . 2 3 1 d 3 3 3 d d 3 e . . . 
            . 2 3 1 3 3 3 3 3 d 1 3 b e . . 
            . 2 1 d 3 3 3 3 d 3 3 1 3 b b . 
            2 3 1 d 3 3 1 1 3 3 3 1 3 4 b b 
            2 d 3 3 d 1 3 1 3 3 3 1 3 4 4 b 
            2 d 3 3 3 1 3 1 3 3 3 1 b 4 4 e 
            2 d 3 3 3 1 1 3 3 3 3 1 b 4 4 e 
            e d 3 3 3 3 d 3 3 3 d d b 4 4 e 
            e d d 3 3 3 d 3 3 3 1 3 b 4 b e 
            e 3 d 3 3 1 d d 3 d 1 b b e e . 
            . e 3 1 1 d d 1 1 1 b b e e e . 
            . . e 3 3 3 3 3 3 b e e e e . . 
            . . . e e e e e e e e e e . . .
    """),
    img("""
        . . . . . . b b b b . . . . . . 
            . . . . . . b 4 4 4 b . . . . . 
            . . . . . . b b 4 4 4 b . . . . 
            . . . . . b 4 b b b 4 4 b . . . 
            . . . . b d 5 5 5 4 b 4 4 b . . 
            . . . . b 3 2 3 5 5 4 e 4 4 b . 
            . . . b d 2 2 2 5 7 5 4 e 4 4 e 
            . . . b 5 3 2 3 5 5 5 5 e e e e 
            . . b d 7 5 5 5 3 2 3 5 5 e e e 
            . . b 5 5 5 5 5 2 2 2 5 5 d e e 
            . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
            . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
            b d 3 2 d 5 5 5 d d d 4 4 . . . 
            b 5 5 5 5 d d 4 4 4 4 . . . . . 
            4 d d d 4 4 4 . . . . . . . . . 
            4 4 4 4 . . . . . . . . . . . .
    """),
    img("""
        . . . . . . . e e e e . . . . . 
            . . . . . e e 4 5 5 5 e e . . . 
            . . . . e 4 5 6 2 2 7 6 6 e . . 
            . . . e 5 6 6 7 2 2 6 4 4 4 e . 
            . . e 5 2 2 7 6 6 4 5 5 5 5 4 . 
            . e 5 6 2 2 8 8 5 5 5 5 5 4 5 4 
            . e 5 6 7 7 8 5 4 5 4 5 5 5 5 4 
            e 4 5 8 6 6 5 5 5 5 5 5 4 5 5 4 
            e 5 c e 8 5 5 5 4 5 5 5 5 5 5 4 
            e 5 c c e 5 4 5 5 5 4 5 5 5 e . 
            e 5 c c 5 5 5 5 5 5 5 5 4 e . . 
            e 5 e c 5 4 5 4 5 5 5 e e . . . 
            e 5 e e 5 5 5 5 5 4 e . . . . . 
            4 5 4 e 5 5 5 5 e e . . . . . . 
            . 4 5 4 5 5 4 e . . . . . . . . 
            . . 4 4 e e e . . . . . . . . .
    """)]
ship = sprites.create(assets.image("""
    plane
"""), SpriteKind.player)
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.move_sprite(ship, 100, 100)
info.set_life(3)
effects.clouds.start_screen_effect()
scene.set_background_color(9)

def on_update_interval():
    global pill
    pill = sprites.create_projectile_from_side(chemical_foods[randint(0, len(chemical_foods) - 1)], 0, 75)
    pill.set_kind(SpriteKind.enemy)
    pill.x = randint(10, 150)
game.on_update_interval(500, on_update_interval)
