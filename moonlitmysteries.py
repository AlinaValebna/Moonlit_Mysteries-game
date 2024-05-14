import pygame
import sys

pygame.init()

# name of the game and icon
pygame.display.set_caption("Moonlit Mysteries")
icon = pygame.image.load('icons/icon_game.png')
pygame.display.set_icon(icon)

# window
screen_width = 1200
screen_height = 750
bottom_panel = 150
screen = pygame.display.set_mode((screen_width, screen_height))

# define colours
colors = [(255, 0, 0), (0, 255, 0), (80, 80, 80)]
red = (255, 0, 0)
green = (0, 255, 0)
grey = (80, 80, 80)
purple = (160, 32, 240)
white = (250, 250, 250)


# load images
bg = pygame.image.load('icons/panel.png').convert_alpha()
panel_img = pygame.image.load('icons/panel.png')
sword_img = pygame.image.load('icons/cursor.png')
spellloading = pygame.image.load('icons/spellloading.png')
spellloading = pygame.transform.scale(spellloading, (80, 80))
sword_attack = pygame.image.load('icons/cursor.png')
potion_img = pygame.image.load('icons/potion.png').convert_alpha()
icon_witch = pygame.image.load('icons/icon_witch.png').convert_alpha()
icon_witch = pygame.transform.scale(icon_witch, (100, 100))
icon_werewolf = pygame.image.load('icons/icon_werewolf.png').convert_alpha()
icon_werewolf = pygame.transform.scale(icon_werewolf, (100, 100))
icon_ghost = pygame.image.load('icons/icon_ghost.png').convert_alpha()
icon_ghost = pygame.transform.scale(icon_ghost, (100, 100))
icon_vampire = pygame.image.load('icons/icon_vampire.png').convert_alpha()
icon_vampire = pygame.transform.scale(icon_vampire, (100, 100))


# load music and sound effects
witchspell = pygame.mixer.Sound('music/spell.wav')
vampirebite = pygame.mixer.Sound('music/vampire_attack.wav')
werewolfroar = pygame.mixer.Sound('music/werewolf_attack.wav')
ghostsigh = pygame.mixer.Sound('music/ghost_attack.wav')
potion = pygame.mixer.Sound('music/potion.wav')
menu_music = pygame.mixer.Sound('music/menu_music.wav')
vampire_music = pygame.mixer.Sound('music/vampire_level.wav')
werewolf_music = pygame.mixer.Sound('music/werewolf_level.wav')
ghost_music = pygame.mixer.Sound('music/ghost_level.wav')
victory_music = pygame.mixer.Sound('music/triumph.wav')
defeat_music = pygame.mixer.Sound('music/darkness.wav')

# global variables
clicked = False
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        clicked = True
    else:
        clicked = False
# clock
FPS = 60
clock = pygame.time.Clock()

# fonts initializing
font = pygame.font.SysFont('Centaur', 24)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# potion button


class Button():
    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                potion.play()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


def draw_bg():
    screen.blit(bg, (0, 0))


def draw_panel():
    # draw panel rectangle
    screen.blit(panel_img, (0, 600))
    # show knight stats
    draw_text(f'{witch.name.upper()}', font,
              grey, 180, screen_height - bottom_panel + 20)


# bg animation


class Animation:
    def __init__(self, name):
        self.name = name
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0

        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/{i}.png')
            image = pygame.transform.scale(image, (1200, 750))
            self.animation_list.append(image)
        self.image = self.animation_list[self.frame_index]

    def draw(self):
        screen.blit(self.image, (0, 0))
        if self.image == self.animation_list[3]:
            self.image = self.animation_list[3]

    def update(self):
        animation_cooldown = 210
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

# healthbars


class Level_animation:
    def __init__(self, name):
        self.name = name
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/{i}.png')
            image = pygame.transform.scale(image, (1200, 600))
            self.animation_list.append(image)
        self.image = self.animation_list[self.frame_index]

    def draw(self):
        screen.blit(self.image, (0, 0))
        if self.image == self.animation_list[3]:
            self.image = self.animation_list[3]

    def update(self):
        animation_cooldown = 210
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0


class Magic_loading_animation:
    def __init__(self, name):
        self.name = name
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/circle_animation/{i}.png')
            image = pygame.transform.scale(image, (84, 84))
            self.animation_list.append(image)
        self.image = self.animation_list[self.frame_index]

    def draw(self):
        screen.blit(self.image, (340, 625))

    def update(self):
        animation_cooldown = 60
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0


class HealthBarPlayer():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        pygame.draw.rect(screen, grey, (self.x, self.y, 180, 15))
        pygame.draw.rect(screen, green, (self.x, self.y,
                         180 * (self.hp / self.max_hp), 15))


class HealthBarEnemy():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        pygame.draw.rect(screen, grey, (self.x, self.y, 180, 15))
        pygame.draw.rect(screen, red, (self.x, self.y,
                         180 * (self.hp / self.max_hp), 15))

# initializing game players


class Supernatural:
    def __init__(self, name, x, y, max_hp, damage, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.potions = potions
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.attack_cooldown = 0
        self.frame_index = 0
        temp_list = []

        # idle animation
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/0idle/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # attack animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/1attack/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # hurt animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/2hurt/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # death animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/3death/{i}.png')
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def cooldown(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        damage = self.damage
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 2*FPS
            self.action = 1
            self.frame_index = 0
            target.hp -= damage
            target.hurt()

    def power_attack(self, target):
        damage = self.damage
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 2*FPS
            self.action = 4
            self.frame_index = 0
            target.hp -= damage
            target.hurt()

    def death(self):
        # set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 240
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()


class Witch(Supernatural):
    def __init__(self, name, x, y, max_hp, damage, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.potions = potions
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.attack_cooldown = 0
        self.frame_index = 0
        temp_list = []

        # idle animation
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/0idle/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # attack animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/1attack/{i}.png')
            image = pygame.transform.scale(image, (180, 280))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # hurt animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/2hurt/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # death animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/3death/{i}.png')
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # power attack animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/4star_power/{i}.png')
            img = pygame.transform.scale(
                img, (750, 250))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target):
        damage = self.damage
        loading.draw()
        loading.update()
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 4*FPS
            self.action = 1
            self.frame_index = 0
            target.hp -= damage
            target.hurt()
            witchspell.play()

    def power_attack(self, target):
        damage = self.damage
        loading.draw()
        loading.update()
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 4*FPS
            self.action = 4
            self.frame_index = 0
            target.hp -= damage
            target.hurt()
            witchspell.play()


class Vampire(Supernatural):
    def __init__(self, name, x, y, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.attack_cooldown = 0
        self.frame_index = 0
        temp_list = []

        # idle animation
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/0idle/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # attack animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/1attack/{i}.png')
            image = pygame.transform.scale(image, (160, 270))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # hurt animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/2hurt/{i}.png')
            image = pygame.transform.scale(image, (160, 250))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # death animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/3death/{i}.png')
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target):
        damage = self.damage
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 4*FPS
            self.action = 1
            self.frame_index = 0
            target.hp -= damage
            target.hurt()
            vampirebite.play()


class Werewolf(Supernatural):
    def __init__(self, name, x, y, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.attack_cooldown = 0
        self.frame_index = 0
        temp_list = []

        # idle animation
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/0idle/{i}.png')
            image = pygame.transform.scale(image, (200, 280))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # attack animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/1attack/{i}.png')
            image = pygame.transform.scale(image, (220, 300))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # hurt animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/2hurt/{i}.png')
            image = pygame.transform.scale(image, (200, 280))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # death animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/3death/{i}.png')
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target):
        damage = self.damage
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 4*FPS
            self.action = 1
            self.frame_index = 0
            target.hp -= damage
            target.hurt()
            werewolfroar.play()


class Ghost(Supernatural):
    def __init__(self, name, x, y, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.attack_cooldown = 0
        self.frame_index = 0
        temp_list = []

        # idle animation
        self.animation_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/0idle/{i}.png')
            image = pygame.transform.scale(image, (200, 280))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # attack animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/1attack/{i}.png')
            image = pygame.transform.scale(image, (220, 300))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # hurt animation
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'images/{self.name}/2hurt/{i}.png')
            image = pygame.transform.scale(image, (200, 280))
            temp_list.append(image)
        self.animation_list.append(temp_list)

        # death animation
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f'images/{self.name}/3death/{i}.png')
            img = pygame.transform.scale(
                img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target):
        damage = self.damage
        if target.hp < 1:
            target.alive = False
            target.death()
        if self.attack_cooldown == 0 and target.alive == True:
            self.attack_cooldown = 4*FPS
            self.action = 1
            self.frame_index = 0
            target.hp -= damage
            target.hurt()
            ghostsigh.play()


# initialization of objects
menuanimation = Animation("menu")
forestanimation = Level_animation('bg_forest')
castleanimation = Level_animation('bg_castle')
cemeteryanimation = Level_animation('bg_cemetery')
werewolfplot = Animation("plot_werewolf")
ghostplot = Animation("plot_ghost")
vampireplot = Animation("plot_vampire")
victoryplot = Animation('plot_victory')
defeatplot = Animation('plot_defeat')
victory_werewolf = Animation(
    'victory_werewolf')
victory_ghost = Animation(
    'victory_ghost')
loading = Magic_loading_animation(
    'circle_animation')
creator = Animation('creator')
witch = Witch("Elara", 180, 430, 50, 10, 3)
vampire = Vampire("vampire", 980, 430, 40, 5)
ghost = Ghost("ghost", 980, 430, 35, 4)
werewolf = Werewolf("werewolf", 980, 430, 30, 3)

witch_healthbar = HealthBarPlayer(150, 670, witch.hp, witch.max_hp)
vampire_healthbar = HealthBarEnemy(
    850, 670, vampire.hp, vampire.max_hp)
werewolf_healthbar = HealthBarEnemy(
    850, 670, werewolf.hp, werewolf.max_hp)
ghost_healthbar = HealthBarEnemy(
    850, 670, ghost.hp, ghost.max_hp)

# create potion button
potion_button = Button(
    screen, 430, 625, potion_img, 80, 80)


class GameState():
    def __init__(self):
        self.state = 'menu'

    def menu(self):
        menu_music.play()
        menu_music.set_volume(0.5)
        run = True
        while run:
            clock.tick(FPS)
            menuanimation.draw()
            menuanimation.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.werewolfplot()

            pygame.display.update()

    def werewolfplot(self):
        run = True
        while run:
            clock.tick(FPS)
            werewolfplot.draw()
            werewolfplot.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)
            menu_music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.werewolf_level()

            pygame.display.update()

    def ghostplot(self):
        run = True
        werewolf_music.stop()
        while run:
            clock.tick(FPS)
            ghostplot.draw()
            ghostplot.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ghost_level()

            pygame.display.update()

    def vampireplot(self):
        ghost_music.stop()
        run = True
        while run:
            clock.tick(FPS)
            vampireplot.draw()
            vampireplot.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vampire_level()

            pygame.display.update()

    def victoryplot(self):
        run = True
        vampire_music.stop()
        victory_music.play()
        # victory_music.set_volume(0.1)
        while run:
            clock.tick(FPS)
            victoryplot.draw()
            victoryplot.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.creator()

            pygame.display.update()

    def creator(self):
        run = True
        while run:
            clock.tick(FPS)
            creator.draw()
            creator.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def defeatplot(self):
        run = True
        vampire_music.stop()
        werewolf_music.stop()
        ghost_music.stop()
        defeat_music.play()
        while run:
            clock.tick(FPS)
            defeatplot.draw()
            defeatplot.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def victory_werewolf(self):
        run = True
        while run:
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            victory_werewolf.draw()
            victory_werewolf.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ghostplot()

            pygame.display.update()

    def victory_ghost(self):
        run = True
        while run:
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            victory_ghost.draw()
            victory_ghost.update()
            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vampireplot()

            pygame.display.update()

    def vampire_level(self):
        run = True
        ghost_music.stop()
        vampire_music.play()
        vampire_music.set_volume(0.5)
        while run:
            global clicked
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            castleanimation.draw()
            castleanimation.update()
            draw_panel()
            screen.blit(spellloading, (343, 625))

            draw_text(vampire.name.upper(), font, grey, 850,
                      (screen_height - bottom_panel + 20))
            witch_healthbar.draw(witch.hp)
            vampire_healthbar.draw(vampire.hp)
            screen.blit(icon_vampire, (1040, 625))
            screen.blit(icon_witch, (43, 625))
            potion = False

            if potion_button.draw():
                potion = True
            draw_text(str(witch.potions), font, white, 492,
                      screen_height - bottom_panel + 30)

            witch.draw()
            witch.update()
            vampire.draw()
            vampire.update()
            vampire.cooldown()
            witch.cooldown()

            # make sure mouse is visible

            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            if potion == True and witch.alive == True:
                if witch.potions > 0:
                    witch.hp += 5
                    witch.potions -= 1

            if vampire.rect.collidepoint(pos) and clicked == True:
                if vampire.alive and witch.alive:
                    witch.power_attack(vampire)
                    draw_text('creating spell', font, white, 210, 300)

            if vampire.alive == True:
                vampire.attack(witch)

            if vampire.alive == False:
                vampire.death()

            if witch.attack_cooldown == 0 and vampire.alive == False:
                witch.attack_cooldown = 4*FPS
                self.victoryplot()

            if witch.alive == False:
                self.defeatplot()
                vampire_music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            pygame.display.update()

    def werewolf_level(self):
        run = True
        werewolf_music.play()
        # werewolf_music.set_volume(0.1)
        while run:
            global clicked
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            forestanimation.draw()
            forestanimation.update()
            draw_panel()
            screen.blit(spellloading, (343, 625))
            draw_text(werewolf.name.upper(), font, grey, 840,
                      (screen_height - bottom_panel + 20))
            witch_healthbar.draw(witch.hp)
            werewolf_healthbar.draw(werewolf.hp)
            potion = False
            screen.blit(icon_werewolf, (1040, 625))
            screen.blit(icon_witch, (43, 625))

            witch.draw()
            witch.update()
            werewolf.draw()
            werewolf.update()
            werewolf.cooldown()
            witch.cooldown()

            # make sure mouse is visible

            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            if potion == True and witch.alive == True:
                if witch.potions > 0:
                    witch.hp += 5
                    witch.potions -= 1

            if werewolf.rect.collidepoint(pos) and clicked == True:
                if werewolf.alive and witch.alive:
                    witch.attack(werewolf)
                    draw_text('creating spell', font, white, 210,
                              300)

            if werewolf.alive == True:
                werewolf.attack(witch)

            if werewolf.alive == False:
                werewolf.death()
            if witch.attack_cooldown == 0 and werewolf.alive == False:
                witch.attack_cooldown = 4*FPS
                self.victory_werewolf()

            if witch.alive == False:
                self.defeatplot()
                werewolf_music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            pygame.display.update()

    def ghost_level(self):
        run = True
        werewolf_music.stop()
        ghost_music.play()
        # ghost_music.set_volume(0.1)
        while run:
            global clicked
            clock.tick(FPS)
            screen.blit(bg, (0, 0))
            cemeteryanimation.draw()
            cemeteryanimation.update()
            draw_panel()
            draw_text(ghost.name.upper(), font, grey, 860,
                      (screen_height - bottom_panel + 20))
            screen.blit(spellloading, (343, 625))
            witch_healthbar.draw(witch.hp)
            ghost_healthbar.draw(ghost.hp)
            screen.blit(icon_ghost, (1040, 625))
            screen.blit(icon_witch, (43, 625))
            potion = False
            if potion_button.draw():
                potion = True
            draw_text(str(witch.potions), font, white, 492,
                      screen_height - bottom_panel + 30)
            witch.draw()
            witch.update()
            ghost.draw()
            ghost.update()
            ghost.cooldown()
            witch.cooldown()

            # make sure mouse is visible

            pos = pygame.mouse.get_pos()
            screen.blit(sword_img, pos)
            pygame.mouse.set_visible(False)

            if potion == True and witch.alive == True:
                if witch.potions > 0:
                    witch.hp += 5
                    witch.potions -= 1

            if ghost.rect.collidepoint(pos) and clicked == True:
                if ghost.alive and witch.alive:
                    witch.attack(ghost)
                    draw_text('creating spell', font, white, 210, 300)

            if ghost.alive == True:
                ghost.attack(witch)

            if ghost.alive == False:
                ghost.death()

            if witch.attack_cooldown == 0 and ghost.alive == False:
                witch.attack_cooldown = 4*FPS
                self.victory_ghost()

            if witch.alive == False:
                self.defeatplot()
                ghost_music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            pygame.display.update()

    def state_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
        if self.state == 'vampire_level':
            self.vampire_level()
        if self.state == 'werewolf_level':
            self.werewolf_level()
        if self.state == 'ghost_level':
            self.ghost_level()
        if self.state == 'menu':
            self.menu()
        if self.state == 'werewolfplot':
            self.werewolfplot()
        if self.state == 'ghostplot':
            self.ghostplot()
        if self.state == 'vampireplot':
            self.vampireplot()
        if self.state == 'victoryplot':
            self.victoryplot()
        if self.state == 'defeatplot':
            self.defeatplot()


game_state = GameState()


def main():
    game_state.state_manager()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
    pygame.display.update()


if __name__ == "__main__":
    main()
