class Device():
    """Basisklasse für alle Smart-Home-Geräte."""

    device_count = 0                        # Klassenattribut
    
    def __init__(self, name, device_type="Device", status=False, ip_address=None):
        self.name = name                    # Instanzattribut
        self.device_type = device_type      # Instanzattribut
        self.status = status                # Instanzattribut
        self.ip_address = ip_address        # Instanzattribut
        Device.device_count += 1

    def get_status(self):
        return "ON" if self.status == True else "OFF"
    
    def turn_on(self):
        self.status = True
        print(f"{self.name}'s status changed to ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name}'s status changed to OFF.")

    def show_commands(self):
        return [
            "turn_on",
            "turn_off",
            "get_status"
        ]


class Thermostat(Device):
    """Spezifische Sub-Klasse für Thermostate."""

    def __init__(self, name, ip_address, target_temp=None):
        super().__init__(name, ip_address=ip_address, device_type="Thermostat")
        self.target_temp = target_temp
        self.actual_temp = None # Sollte vom realen Gerät abgefragt werden

    def set_target_temp(self, temp):
        self.target_temp = temp
        print(f"{self.name}'s target temperature set to {self.target_temp}°C.")
        # Hier Befehle für das reale Gerät hinzufügen, um die Temperatur zu setzen

    def get_actual_temp(self):
        print(f"{self.name}'s actual temperature is {self.actual_temp}°C.")

    def show_commands(self):
        return [
            "turn_on",
            "turn_off",
            "get_status",
            "set_target_temp",
            "get_actual_temp"
        ]

class SmartLight(Device):
    """Spezifische Sub-Klasse für Lampen."""

    def __init__(self, name, ip_address, brightness=100, color="white"):
        super().__init__(name, ip_address=ip_address, device_type="SmartLight")
        self.brightness = brightness
        self.color = color

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"{self.name}'s brightness set to {self.brightness}%.")

    def set_color(self, color):
        self.color = color
        print(f"{self.name}'s color set to {self.color}.")

    def turn_on(self):
        self.set_brightness(100)
        self.set_color("white")
        self.status = True

    def show_commands(self):
        return [
            "turn_on",
            "turn_off",
            "get_status",
            "set_brightness",
            "set_color"
        ]

class SecurityCamera(Device):
    """Spezifische Sub-Klasse für Sicherheitskameras."""

    def __init__(self, name, ip_address, resolution="1080p"):
        super().__init__(name, ip_address=ip_address, device_type="SecurityCamera")
        self.resolution = resolution
        self.recording = False

    def set_resolution(self, resolution):
        self.resolution = resolution
        print(f"{self.name}'s resolution set to {self.resolution}.")
    
    def start_recording(self):
        self.recording = True
        print(f"{self.name} is now recording.")
    
    def stop_recording(self):
        self.recording = False
        print(f"{self.name} has stopped recording.")

    def show_commands(self):
        return [
            "turn_on",
            "turn_off",
            "get_status",
            "set_resolution",
            "start_recording",
            "stop_recording"
        ]