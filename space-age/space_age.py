class SpaceAge:
    def __init__(self, seconds: int):
        self.seconds: float = float(seconds)
        self.year_in_seconds_on_earth: float = 31557600.0
        self.mercury_year: float = 0.2408467
        self.venus_year: float = 0.61519726
        self.earth_year: float = 1.0
        self.mars_year: float = 1.8808158
        self.jupiter_year: float = 11.862615
        self.saturn_year: float = 29.447498
        self.uranus_year: float = 84.016846
        self.neptune_year: float = 164.79132

    def on_mercury(self) -> float:
        return round(
            self.seconds / self.year_in_seconds_on_earth / self.mercury_year, 2
        )

    def on_venus(self) -> float:
        return round(self.seconds / self.year_in_seconds_on_earth / self.venus_year, 2)

    def on_earth(self) -> float:
        return round(self.seconds / self.year_in_seconds_on_earth / self.earth_year, 2)

    def on_mars(self) -> float:
        return round(self.seconds / self.year_in_seconds_on_earth / self.mars_year, 2)

    def on_jupiter(self) -> float:
        return round(
            self.seconds / self.year_in_seconds_on_earth / self.jupiter_year, 2
        )

    def on_saturn(self) -> float:
        return round(self.seconds / self.year_in_seconds_on_earth / self.saturn_year, 2)

    def on_uranus(self) -> float:
        return round(self.seconds / self.year_in_seconds_on_earth / self.uranus_year, 2)

    def on_neptune(self) -> float:
        return round(
            self.seconds / self.year_in_seconds_on_earth / self.neptune_year, 2
        )
