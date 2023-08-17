import pygame
import os

# Global Constants
TITLE = "Runner Guy"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Personagem/parado/Parado1.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/Correndo6.png")),
]

RUNNING_SHIELD = [

    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/CorrendoPowerup2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/CorrendoPowerup3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/CorrendoPowerup4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/CorrendoPowerup5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/correndo/CorrendoPowerup6.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulando1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulando2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulando3.png")),           
]
JUMPING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulandoshield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulandoshield2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/pulando/pulandoshield3.png")),
]
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/abaixando/abaixando1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/abaixando/abaixando1.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/abaixando/abaixandoshield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Personagem/abaixando/abaixandoshield1.png")),
    ]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
