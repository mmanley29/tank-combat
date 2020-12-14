import random
import arcade
import math 
from arcade.draw_commands import draw_texture_rectangle




SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.25
SCREEN_TITLE = "Atari 2600 Combat"

# Sprite Constants
CHARACTER_SCALING = .5
TILE_SCALING = 0.25
PLAYER_MOVEMENT_SPEED = 2
ANGLE_SPEED = 1
GRAVITY = 0

#Health Bar 

HEALTHBAR_Y_OFFSET = 40
HEALTHBAR_X_OFFSET = 10
HEALTHBAR_HEIGHT = 30
HEALTHBAR_PADDING = 5
HEALTHBAR_WIDTH = 300
HEALTHBAR_X = HEALTHBAR_WIDTH

class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('tank.jpg')
    
    def on_show(self):

        arcade.set_viewport(0, SCREEN_WIDTH -1, 0, SCREEN_HEIGHT -1)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH /2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Click to Start Combat ", SCREEN_WIDTH/2, SCREEN_HEIGHT /2-75, arcade.color.WHITE, font_size=20, anchor_x="center")

        start_x = 50
        start_y = 400
        start_x1 = 650
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Player 1 Controls.",
                         80, start_y, arcade.color.BLACK, 18, anchor_x="left", anchor_y="top")
        # arcade.draw_text("UP DOWN LEFT RIGHT ARROW KEYS", 170,340, arcade.color.BLACK,18,anchor_x="center")
        arcade.draw_text("UP",170,340,arcade.color.BLACK,16,anchor_x="center")
        arcade.draw_text("LEFT",70,300,arcade.color.BLACK,16,anchor_x="left")
        arcade.draw_text("RIGHT",290,300,arcade.color.BLACK,16,anchor_x="right")
        arcade.draw_text("DOWN",170,300,arcade.color.BLACK,16,anchor_x="center")



        arcade.draw_point(start_x1, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Player 2 Controls.",
                         720, start_y, arcade.color.BISQUE, 18, anchor_x="left", anchor_y="top")
        arcade.draw_text("W",780,340,arcade.color.BISQUE,16,anchor_x="center")
        arcade.draw_text("A",720,300,arcade.color.BISQUE,16,anchor_x="left")
        arcade.draw_text("D",850,300,arcade.color.BISQUE,16,anchor_x="right")
        arcade.draw_text("S",780,300,arcade.color.BISQUE,16,anchor_x="center")
        

    def on_mouse_press(self, _x, _y,_button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class GameOverview(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('tank.jpg')
    
    def on_show(self):

        arcade.set_viewport(0, SCREEN_WIDTH -1, 0, SCREEN_HEIGHT -1)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH /2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Game Over - Click to Restart ", SCREEN_WIDTH/2, SCREEN_HEIGHT /2-75, arcade.color.WHITE, font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y,_button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class Player(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 0

    def update(self):
        angle_rad = math.radians(self.angle)

        self.angle += self.change_angle

        self.center_x = self.center_x + -self.speed*math.sin(angle_rad)
        self.center_y = self.center_y + self.speed*math.cos(angle_rad)


class GameView(arcade.View):
    """ Our custom Window Class"""
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Keeps track of sprites
        self.wall_list = None
        self.player1_list = None
        self.player2_list = None

        # holds player sprite
        self.player_sprite1 = None
        self.player_sprite2 = None
        
        self.player1_health = 100
        self.player2_health = 100

    def setup(self):
        # call this function to restart the game
        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.player1_bullet_list = arcade.SpriteList()
        self.player2_bullet_list = arcade.SpriteList()

        # setup player sprite and starting coordinates
        image_source = "tank_sprite.jpg"
        self.player_sprite1 = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite1 = Player(image_source, CHARACTER_SCALING)
        self.player_sprite1.center_x = 100
        self.player_sprite1.center_y = 325
        self.player1_list.append(self.player_sprite1)

        image_source = "tank_sprite.jpg"
        self.player_sprite2 = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite2 = Player(image_source, CHARACTER_SCALING)
        self.player_sprite2.center_x = 900
        self.player_sprite2.center_y = 325
        self.player2_list.append(self.player_sprite2)

        # creating field
        coordinate_list = [[200, 100],
                           [228, 100],
                           [256, 100],
                           [200, 297],
                           [200, 325],
                           [200, 353],
                           [200, 550],
                           [228, 550],
                           [256, 550],
                           [300, 325],
                           [400, 150],
                           [428, 150],
                           [456, 150],
                           [400, 178],
                           [400, 206],
                           [400, 444],
                           [400, 472],
                           [400, 500],
                           [428, 500],
                           [456, 500],
                           [500, 14],
                           [500, 636],
                           [500, 325],
                           [600, 150],
                           [572, 150],
                           [544, 150],
                           [600, 178],
                           [600, 178],
                           [600, 206],
                           [600, 444],
                           [600, 472],
                           [600, 500],
                           [572, 500],
                           [544, 500],
                           [800, 100],
                           [772, 100],
                           [744, 100],
                           [800, 325],
                           [800, 550],
                           [772, 550],
                           [744, 550],
                           ]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/brickGrey.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        # Create the 'physics engine'
        self.physics_engine1 = arcade.PhysicsEnginePlatformer(
            self.player_sprite1, self.wall_list, GRAVITY)
        self.physics_engine2 = arcade.PhysicsEnginePlatformer(
            self.player_sprite2, self.wall_list, GRAVITY)

    def on_draw(self):
        # drawing the screen
        arcade.start_render()
        self.wall_list.draw()
        self.player1_list.draw()
        self.player2_list.draw()
        self.player1_bullet_list.draw()
        self.player2_bullet_list.draw()

        arcade.draw_text("Player 1 ", 150, 10, arcade.color.WHITE, font_size=20, anchor_x="right")

        arcade.draw_text("Player 2 ", 850, 10, arcade.color.WHITE, font_size=20, anchor_x="left")


        arcade.draw_rectangle_filled(center_x=HEALTHBAR_X, center_y=20, width=((HEALTHBAR_WIDTH-HEALTHBAR_PADDING)*self.player1_health/100)//1, height=HEALTHBAR_HEIGHT-HEALTHBAR_PADDING, color=arcade.color.GREEN)
        arcade.draw_rectangle_filled(center_x=700, center_y=20, width=((HEALTHBAR_WIDTH-HEALTHBAR_PADDING)*self.player2_health/100)//1, height=HEALTHBAR_HEIGHT-HEALTHBAR_PADDING, color=arcade.color.GREEN)

    # player movement when key pressed

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # sprite 1 movement
        if key == arcade.key.W:
            self.player_sprite1.speed = PLAYER_MOVEMENT_SPEED
        #elif key == arcade.key.DOWN:
            #self.player_sprite1.speed = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.A:
            self.player_sprite1.change_angle = ANGLE_SPEED
        elif key == arcade.key.D:
            self.player_sprite1.change_angle = -ANGLE_SPEED

        # sprite 2 movement
        if key == arcade.key.UP:
            self.player_sprite2.speed = PLAYER_MOVEMENT_SPEED
        #elif key == arcade.key.S:
            #self.player_sprite2.speed = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.player_sprite2.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite2.change_angle = -ANGLE_SPEED

        if key == arcade.key.DOWN:
            if len(self.player2_bullet_list) < 1:
                bullet_sprite = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", CHARACTER_SCALING)
                bullet_sprite.guid = "Bullet"

                bullet_sprite.center_x = self.player_sprite2.center_x
                bullet_sprite.center_y = self.player_sprite2.center_y
                bullet_sprite.update()

                bullet_speed = 5
                bullet_sprite.change_y = \
                    math.cos(math.radians(self.player_sprite2.angle)) * bullet_speed
                bullet_sprite.change_x = \
                    -math.sin(math.radians(self.player_sprite2.angle)) \
                    * bullet_speed

                bullet_sprite.angle = self.player_sprite2.angle + 90

                self.player2_bullet_list.append(bullet_sprite)

        if key == arcade.key.S:
            if len(self.player1_bullet_list) < 1:
                bullet_sprite = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", CHARACTER_SCALING)
                bullet_sprite.guid = "Bullet"

                bullet_sprite.center_x = self.player_sprite1.center_x
                bullet_sprite.center_y = self.player_sprite1.center_y
                bullet_sprite.update()

                bullet_speed = 5
                bullet_sprite.change_y = \
                    math.cos(math.radians(self.player_sprite1.angle)) * bullet_speed
                bullet_sprite.change_x = \
                    -math.sin(math.radians(self.player_sprite1.angle)) \
                    * bullet_speed

                bullet_sprite.angle = self.player_sprite1.angle + 90

                self.player1_bullet_list.append(bullet_sprite)


    # player movement when key lifted
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.player_sprite1.speed = 0
        elif key == arcade.key.S:
            self.player_sprite1.speed = 0
        elif key == arcade.key.A:
            self.player_sprite1.change_angle = 0
        elif key == arcade.key.D:
            self.player_sprite1.change_angle = 0

        if key == arcade.key.UP:
            self.player_sprite2.speed = 0
        elif key == arcade.key.DOWN:
            self.player_sprite2.speed = 0
        elif key == arcade.key.LEFT:
            self.player_sprite2.change_angle = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite2.change_angle = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine1.update()
        self.physics_engine2.update()
        self.player1_list.update()
        self.player2_list.update()
        self.player1_bullet_list.update()
        self.player2_bullet_list.update()

        for bullet in self.player1_bullet_list:
            walls = arcade.check_for_collision_with_list(bullet, self.wall_list)
            
            for wall in walls:
                bullet.remove_from_sprite_lists()

            sprites = arcade.check_for_collision_with_list(bullet, self.player2_list)

            for sprite in sprites:
                bullet.remove_from_sprite_lists()
                self.player1_health += -50

                if self.player1_health == 0:
                    print("Player 2 has won!!!")

                    end_screen = GameOverview()
                    window = arcade.window_commands.get_window()
                    window.show_view(end_screen)


            size = max(bullet.width, bullet.height)
            if bullet.center_x < 0 - size:
                bullet.remove_from_sprite_lists()
            if bullet.center_x > SCREEN_WIDTH + size:
                bullet.remove_from_sprite_lists()
            if bullet.center_y < 0 - size:
                bullet.remove_from_sprite_lists()
            if bullet.center_y > SCREEN_HEIGHT + size:
                bullet.remove_from_sprite_lists()
        
        for bullet in self.player2_bullet_list:
            walls = arcade.check_for_collision_with_list(bullet, self.wall_list)
            
            for wall in walls:
                bullet.remove_from_sprite_lists()
            
            sprites = arcade.check_for_collision_with_list(bullet, self.player1_list)

            for sprite in sprites:
                bullet.remove_from_sprite_lists()
                self.player2_health += -50
            
                if self.player2_health == 0:
                    print("Player 1 has won!!!")

                    end_screen = GameOverview()
                    window = arcade.window_commands.get_window()
                    window.show_view(end_screen)


            size = max(bullet.width, bullet.height)
            if bullet.center_x < 0 - size:
                bullet.remove_from_sprite_lists()
            if bullet.center_x > SCREEN_WIDTH + size:
                bullet.remove_from_sprite_lists()
            if bullet.center_y < 0 - size:
                bullet.remove_from_sprite_lists()
            if bullet.center_y > SCREEN_HEIGHT + size:
                bullet.remove_from_sprite_lists()



def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()
        


if __name__ == "__main__":
    main()