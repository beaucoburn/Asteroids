class Player(CircleShape):
    def __init__(self, x, y)
        super().__init__(self, PLAYER_RADIUS)
        self.y = y
        self.x = x
        self.PLAYER_RADIUS = PLAYER_RADIUS
        rotation = 0

        def triangle(self):
            forward = pygame.Vector2(0,1).rotate(self.rotation)
            right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.postion + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]

        def draw(self, screen):
            pygame.draw.polygon(screen, self.color("white"), self.triangle(2))
