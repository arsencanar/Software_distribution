import pygame

# Инициализация Pygame
pygame.init()

# Размер окна
WINDOW_SIZE = (700, 500)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)

# Установка заголовка окна
pygame.display.set_caption('Догонялки')

# Загрузка фона
background = pygame.image.load('background.png').convert()

# Изменение размеров фона
background = pygame.transform.scale(background, (700, 500))

# Загрузка спрайтов
sprite1 = pygame.image.load('sprite1.png')
sprite2 = pygame.image.load('sprite2.png')

# Изменение размеров спрайтов
sprite1 = pygame.transform.scale(sprite1, (50, 50))
sprite2 = pygame.transform.scale(sprite2, (50, 50))

# Создание объектов спрайтов
sprite1_obj = pygame.sprite.Sprite()
sprite1_obj.image = sprite1
sprite1_obj.rect = sprite1.get_rect()
sprite1_obj.rect.x = 200
sprite1_obj.rect.y = 400

sprite2_obj = pygame.sprite.Sprite()
sprite2_obj.image = sprite2
sprite2_obj.rect = sprite2.get_rect()
sprite2_obj.rect.x = 300
sprite2_obj.rect.y = 400

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1_obj)
all_sprites.add(sprite2_obj)

# Создание объекта clock для установки FPS
clock = pygame.time.Clock()
# Константа FPS
FPS = 60

# Игровой цикл
game_running = True
while game_running:
    # Проверка на событие закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Получение словаря нажатых клавиш
    keys_pressed = pygame.key.get_pressed()

    # Проверка на нажатие клавиш и перемещение спрайтов
    if keys_pressed[pygame.K_LEFT] and sprite1_obj.rect.x > 0:
        sprite1_obj.rect.move_ip(-5, 0)
    if keys_pressed[pygame.K_RIGHT] and sprite1_obj.rect.x < WINDOW_SIZE[0] - sprite1_obj.rect.width:
        sprite1_obj.rect.move_ip(5, 0)
    if keys_pressed[pygame.K_UP] and sprite1_obj.rect.y > 0:
        sprite1_obj.rect.move_ip(0, -5)
    if keys_pressed[pygame.K_DOWN] and sprite1_obj.rect.y < WINDOW_SIZE[1] - sprite1_obj.rect.height:
        sprite1_obj.rect.move_ip(0, 5)

    if keys_pressed[pygame.K_a] and sprite2_obj.rect.x > 0:
        sprite2_obj.rect.move_ip(-5, 0)
    if keys_pressed[pygame.K_d] and sprite2_obj.rect.x < WINDOW_SIZE[0] - sprite2_obj.rect.width:
        sprite2_obj.rect.move_ip(5, 0)
    if keys_pressed[pygame.K_w] and sprite2_obj.rect.y > 0:
        sprite2_obj.rect.move_ip(0, -5)
    if keys_pressed[pygame.K_s] and sprite2_obj.rect.y < WINDOW_SIZE[1] - sprite2_obj.rect.height:
        sprite2_obj.rect.move_ip(0, 5)

    # Рисование фона
    screen.blit(background, (0, 0))

    # Рисование всех спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.update()

    # Установка частоты смены кадров
    clock.tick(FPS)

    # Проверка на нажатие на кнопку "Закрыть окно"
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] > WINDOW_SIZE[0]-50 and pygame.mouse.get_pos()[1] < 50:
            game_running = False

# Выход из игры
pygame.quit()