class Device():
    """Basic Class for all Smart Home devices."""

    device_count = 0                        # Klassenattribut
    
    def __init__(self, name, device_type="Device", status=True, ip_address=None):
        self.name = name                    # Instanzattribut
        self.device_type = device_type      # Instanzattribut
        self.status = status                # Instanzattribut
        self.ip_address = ip_address        # Instanzattribut
        self.commands = [
            "turn_on",
            "turn_off",
            "get_status",
            "set_ip_address"
        ]                                   # Instanzattribut
        Device.device_count += 1            # Zugriff auf Klassenattribut

    def get_status(self):
        return "ON" if self.status == True else "OFF"
    
    def turn_on(self):
        self.status = True
        print(f"{self.name}'s status changed to ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name}'s status changed to OFF.")

    @classmethod
    def get_device_count(cls):
        return cls.device_count
    
    @staticmethod
    def is_valid_ipv4(ip_address):
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                return False
        return True
    
    def set_ip_address(self, ip_address):
        if ip_address is None or self.is_valid_ipv4(ip_address):
            self.ip_address = ip_address
            print(f"{self.name}'s IP address set to {self.ip_address}.")
        else:
            print(f"Invalid IP address: {ip_address}")

    def show_commands(self):
        return self.commands


class Thermostat(Device):
    """Specific Sub-Class for Thermostats."""

    def __init__(self, name, ip_address, target_temp=None):
        super().__init__(name, ip_address=ip_address, device_type="Thermostat")
        self.target_temp = target_temp
        self.actual_temp = None # Should be queried from the real device
        self.commands.extend([
            "set_target_temp",
            "get_actual_temp"
        ])

    def set_target_temp(self, temp):
        self.target_temp = temp
        print(f"{self.name}'s target temperature set to {self.target_temp}°C.")
        # Here add commands for the real device to set the temperature

    def get_actual_temp(self):
        print(f"{self.name}'s actual temperature is {self.actual_temp}°C.")

    def show_commands(self):
        return self.commands


class SmartLight(Device):
    """Specific Sub-Class for Smart Lights."""

    def __init__(self, name, ip_address, brightness=100, color="white"):
        super().__init__(name, ip_address=ip_address, device_type="SmartLight")
        self.brightness = brightness
        self.color = color
        self.commands.extend([
            "set_brightness",
            "set_color"
        ])

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
        return self.commands


class SecurityCamera(Device):
    """Specific Sub-Class for Security Cameras."""

    def __init__(self, name, ip_address, resolution="1080p"):
        super().__init__(name, ip_address=ip_address, device_type="SecurityCamera")
        self.resolution = resolution
        self.recording = False
        self.commands.extend([
            "set_resolution",
            "start_recording",
            "stop_recording"
        ])

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
        return self.commands