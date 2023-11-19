pcShipPlayer1 = sprites.create(assets.image("""
    pcShip
"""), SpriteKind.player)
pcShipPlayer2 = sprites.create(assets.image("""
    npcShipBlob
"""), SpriteKind.player)
pcShipPlayer1.set_position(5, scene.screen_height() / 2)
pcShipPlayer2.set_position(scene.screen_width() - 5, scene.screen_height() / 2)

def on_forever():
    controller.player1.move_sprite(pcShipPlayer1)
    controller.player2.move_sprite(pcShipPlayer2)
forever(on_forever)
