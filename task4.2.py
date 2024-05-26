class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # Default price
        self.inches = 0  # Default inches
        self.on = False  # Default off
        self.volume = 50  # Default volume

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LED(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"Screen thickness: {self.screen_thickness} inches, Energy usage: {self.energy_usage}, Lifespan: {self.lifespan} years, Refresh rate: {self.refresh_rate} Hz"


class Plasma(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"Screen thickness: {self.screen_thickness} inches, Energy usage: {self.energy_usage}, Lifespan: {self.lifespan} years, Refresh rate: {self.refresh_rate} Hz, Viewing angle: {self.viewing_angle}, Backlight: {self.backlight}"


# Example usage:
led_tv = LED("Sony", 0.5, "Low", 5, 120)
led_tv.set_channel(10)
led_tv.increase_volume()
print(led_tv.status())
print(led_tv.display_details())

plasma_tv = Plasma("Samsung", 1.0, "High", 7, 60, "Wide", "LED")
plasma_tv.set_channel(20)
plasma_tv.decrease_volume()
print(plasma_tv.status())
print(plasma_tv.display_details())
