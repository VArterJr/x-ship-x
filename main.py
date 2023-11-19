pcShipPlayer1 = sprites.create(assets.image("""
    pcShip
"""), SpriteKind.player)
pcShipPlayer2 = sprites.create(assets.image("""
    npcShipBlob
"""), SpriteKind.player)
pcShipPlayer1.set_position(0, scene.screen_height() / 2 + 5)
pcShipPlayer2.set_position(scene.screen_width() - 5, scene.screen_height() / 2 + 5)

def on_forever():
    controller.player1.move_sprite(pcShipPlayer2)
    controller.player2.move_sprite(pcShipPlayer2)
forever(on_forever)
