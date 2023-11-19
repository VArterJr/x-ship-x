let pcShip = sprites.create(assets.image`pcShip`, SpriteKind.Player)
pcShip.setPosition(0, scene.screenHeight() / 2 + 1)
let npcEnemyShip = sprites.create(assets.image`npcShipBlob`, SpriteKind.Enemy)
npcEnemyShip.setPosition(scene.screenWidth() - 1, randint(0, scene.screenHeight()))
forever(function () {
    controller.moveSprite(pcShip)
})
