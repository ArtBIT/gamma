import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add images
#

gamma.resourceManager.addImage('tile_grass', os.path.join('images', 'textures/grass.png'))
gamma.resourceManager.addImage('tile_water', os.path.join('images', 'textures/water.png'))

#
# add some tiles
#

gamma.tileManager.addTile(gamma.Tile('grass', gamma.resourceManager.getImage('tile_grass'), True))
gamma.tileManager.addTile(gamma.Tile('water', gamma.resourceManager.getImage('tile_water'), False))

#
# create a map and add to scene
#

mainScene.world.setMap(gamma.Map(tiles=[ ['grass' for i in range(10)] for j in range(10) ]))
#map = mainScene.world.loadMap('filename.extension')
mainScene.world.map.setTile(3,3,'water')

#
# create a camera
#

worldCameraEntity = gamma.Entity(
    gamma.CameraComponent(0, 0, 600, 400, bgColour=gamma.DARK_GREY)
)
worldCameraEntity.getComponent('camera').setPosition(300, 200)

#
# add camera to world
#

mainScene.world.entities.append(worldCameraEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Map Example')
gamma.sceneManager.push(mainScene)
#mainScene.world.saveMap(map, 'filename.extension')
gamma.run()