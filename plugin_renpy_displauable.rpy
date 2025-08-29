

init python:

    class InfiniteSpiral(renpy.Displayable):
        def __init__(self, image, count=26, max_radius=250, max_size=128, spin_speed=6.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Inicializar partículas distribuidas
            for i in range(count):
                angle = (i / count) * 2 * math.pi
                scale = random.uniform(0.5, 1.0)
                self.particles.append({
                    "angle": angle,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time

            rv = renpy.Render(width, height)

            for p in self.particles:
                # Movimiento circular + expansión/contracción cíclica
                # Usamos un seno para que se acerquen y se alejen constantemente
                phase = (elapsed * 0.5) % 1.0  # 0 → 1 en bucle
                radius = self.max_radius * abs(math.sin(phase * math.pi))

                # Ángulo base + giro infinito
                angle = p["angle"] + self.spin_speed * elapsed

                x = int(math.cos(angle) * radius)
                y = int(math.sin(angle) * radius)

                # Partículas con tamaño "palpitante"
                size_factor = 0.5 + 0.5 * math.sin(elapsed * 2 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)
 
                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.01)
            return rv



init python:

    class ChaoticSpiral(renpy.Displayable):
        def __init__(self, image, count=25, max_radius=300, max_size=64, spin_speed=4.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Punto de fuga aleatorio (puede ser dentro o fuera del centro)
            self.focal_x = random.randint(-100, 100)
            self.focal_y = random.randint(-100, 100)

            # Configurar partículas con propiedades aleatorias
            for i in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0.5, 1.5)     # cada una se expande a distinta velocidad
                spin_offset = random.uniform(-2, 2)  # diferencia en el giro
                scale = random.uniform(0.4, 1.2)
                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "spin_offset": spin_offset,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            rv = renpy.Render(width, height)

            for p in self.particles:
                # Expansión radial caótica
                radius = self.max_radius * abs(math.sin(elapsed * p["speed"]))  # cada partícula late distinto

                # Ángulo base + giro infinito (desfasado por spin_offset)
                angle = p["angle"] + (self.spin_speed + p["spin_offset"]) * elapsed

                # Posición con punto de fuga (focal_x / focal_y)
                x = int(self.focal_x + math.cos(angle) * radius)
                y = int(self.focal_y + math.sin(angle) * radius)

                # Partículas con tamaño aleatorio + oscilación
                size_factor = 0.6 + 0.4 * math.sin(elapsed * 3 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)

                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv

