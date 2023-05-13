class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super ().__init__()
        self.image = transform.scale(image. load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class   Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 2:
            self.rect.x -= 5
        if keys_pressed[K_b] and self.rect.x < 620:
            self.rect.x += 5

class   ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)











game = True
безымянный = ball('Ground 1 (1).png',255,250,4)


p1 = Player('Rectangle 1 (1).png',3,250,2)
p2 = Player('Rectangle 1 (1).png',515,250,2)









speed_x = 3
speed_y = 3

while game:

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y


    if sprite.collide_rect(racket1, ball)
        or sprite.collide_rect(racket2, ball):
                speed_x *= -1



