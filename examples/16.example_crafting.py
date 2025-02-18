import gamma
import os

#
# create a main scene
#

mainScene = gamma.Scene()

#
# add some resources
#

gamma.resourceManager.addImage('player_idle_1', os.path.join('images', 'player', 'vita_00.png'))
gamma.resourceManager.addImage('heart', os.path.join('images', 'heart.png'))

#
# create a player entity
#

# player controls = left and right to move
def playerControls(player):
    if gamma.inputManager.isDown(player.getComponent('input').left):
        player.getComponent('position').rect.x -= 2
    if gamma.inputManager.isDown(player.getComponent('input').right):
        player.getComponent('position').rect.x += 2

playerEntity = gamma.Entity(
    gamma.TagsComponent('player'),
    gamma.PositionComponent(0, 0, 45, 51, z=10),
    gamma.ImageGroupsComponent('idle', gamma.ImageGroup(gamma.resourceManager.getImage('player_idle_1'))),
    # triggers only work on entities with a collider
    gamma.ColliderComponent(0, 0, 45, 51),
    gamma.InputComponent(
        left=gamma.keys.a, right=gamma.keys.d,
        up=gamma.keys.w, down=gamma.keys.s,
        b1=gamma.keys.q, b2=gamma.keys.e,
        b3=gamma.keys.j, b4=gamma.keys.l,
        b5=gamma.keys.k,
        inputContext=playerControls
    )
)

# add a camera to the player
playerEntity.addComponent(gamma.CameraComponent(
    0, 0, 600, 400,
    bgColour = gamma.BLUE
))

# add an invemtory component to the player
playerEntity.addComponent(
    gamma.InventoryComponent(
        20, 20,
        slots=3
    )
)

# add a crafting component to the player
playerEntity.addComponent(
    gamma.CraftingComponent(
        200, 20,
        playerEntity, mainScene,
        slots=3,
        left=playerEntity.getComponent('input').b3,
        right=playerEntity.getComponent('input').b4,
        craft=playerEntity.getComponent('input').b5
    )
)

#
# create a trigger to collect hearts
#

# create a trigger subclass for collecting a heart

class CollectHeartTrigger(gamma.Trigger):
    def onCollide(self, entity, otherEntity):
        if otherEntity.getComponent('tags').has('player'):
            mainScene.world.deleteEntity(entity)
            otherEntity.getComponent('inventory').addEntity('heart')

# add a heart to the entity factory

def createHeart(x, y):
    heartEntity = gamma.Entity()
    heartEntity.addComponent(gamma.PositionComponent(x, y, 27, 30))
    heartEntity.addComponent(gamma.ImageGroupsComponent('idle', gamma.ImageGroup(gamma.resourceManager.getImage('heart'))))
    heartEntity.addComponent(gamma.TriggersComponent(CollectHeartTrigger(boundingBox=gamma.PositionComponent(0,0,27,30), buttonPress='up')))
    return heartEntity

gamma.entityFactory.addEntity('heart', createHeart)

# add some hearts to the player inventory
for i in range(15):
    playerEntity.getComponent('inventory').addEntity('heart')

# add a heart to the world
he = gamma.entityFactory.create('heart', 50, 0)
mainScene.world.entities.append(he)

#
# crafting
#

recipe = gamma.CraftingRecipe(
    'heart',
    ('heart', 1),
    ('heart', 2),
    ('heart', 3)
)
playerEntity.getComponent('crafting').addRecipe(recipe)

#
# add entities to scene's world
#

mainScene.world.entities.append(playerEntity)

#
# add scene to the gamma and start
#

gamma.init((600, 400), caption='Gamma // Crafting Example')
gamma.sceneManager.push(mainScene)
gamma.run()