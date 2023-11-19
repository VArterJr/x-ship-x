pcShip = sprites.create(assets.image("""
    pcShip
"""), SpriteKind.player)
pcShip.set_position(0, (scene.screen_height() / 2 )+1)
npcEnemyShip = sprites.create(assets.image("""
    npcShipBlob
"""), SpriteKind.enemy)
npcEnemyShip.set_position(scene.screen_width()-1, randint(0, scene.screen_height()))

def on_forever():
    controller.move_sprite(pcShip)
forever(on_forever)
