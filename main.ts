let pcShipPlayer1 = sprites.create(assets.image`pcShip`, SpriteKind.Player)
let pcShipPlayer2 = sprites.create(assets.image`npcShipBlob`, SpriteKind.Player)
pcShipPlayer1.setPosition(5, scene.screenHeight() / 2 + 5)
pcShipPlayer2.setPosition(scene.screenWidth() - 5, scene.screenHeight() / 2 + 5)
forever(function () {
    controller.player1.moveSprite(pcShipPlayer1)
    controller.player2.moveSprite(pcShipPlayer2)
})
