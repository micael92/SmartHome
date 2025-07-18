from datetime import datetime

class HTMLGenerator():
    """Generates HTML representation of the Smart Home status."""

    def __init__(self, devices):
        self.devices = devices
        with open("template.html", "r", encoding="utf-8") as f:
            self.template = f.read()

    def generate_html(self):
        device_html = ""

        for d in self.devices:
            status_class = "on" if d.status else "off"
            device_html += f"<div class='device {status_class}'>"
            device_html += f"<strong>{d.name}</strong> ({d.device_type})<br>"
            device_html += f"Status: {d.get_status()}<br>"
            device_html += f"IP-Adresse: {d.ip_address}<br>"

            if hasattr(d, 'target_temp'):
                device_html += f"Zieltemperatur: {d.target_temp}°C<br>"
            if hasattr(d, 'actual_temp'):
                device_html += f"Aktuelle Temperatur: {d.actual_temp}°C<br>"
            if hasattr(d, 'brightness'):
                device_html += f"Helligkeit: {d.brightness}%<br>"
            if hasattr(d, 'color'):
                device_html += f"Farbe: {d.color}<br>"
            if hasattr(d, 'resolution'):
                device_html += f"Auflösung: {d.resolution}<br>"
            if hasattr(d, 'recording'):
                device_html += f"Aufnahme: {'Aktiv' if d.recording else 'Inaktiv'}<br>"

            device_html += "</div>"
        
        with open("smarthome_status.html", "w", encoding="utf-8") as f:
            f.write(self.template.format(
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                device_html=device_html
            ))
        
        #print("HTML file generated: smarthome_status.html")


class CLI():

    """Command Line Interface for the Smart Home Controller."""

    def __init__(self, controller):
        self.controller = controller

    def run(self):
        try:
            
            while True:
                HTMLGenerator(self.controller.devices).generate_html()
    
                print("\033[1;32m\n=== Smart Home Controller CLI ===\033[0m")
                print("Wählen Sie das zu steuernde Gerät:\n")
    
                for i, device in enumerate(self.controller.devices, start=1):
                    print(f"{i}. {device.name} (Status: {device.get_status()})")
    
                print("\n.. oder Beenden Sie das Programm mit Strg + C.\n")
    
                device_index = int(input("Geben Sie die Nummer des Geräts ein: ")) - 1
                print(f"Verfügbare Befehle für {self.controller.devices[device_index].name}:")
                commands = self.controller.devices[device_index].show_commands()
                for i, command in enumerate(commands, start=1):
                    print(f"{i}. {command}")
    
                command_index = int(input("Geben Sie die Nummer des Befehls ein: ")) - 1
                command = commands[command_index]
                print(f"Sie haben den Befehl '{command}' ausgewählt.")
    
                if "set" in command:
                    if "temp" in command:
                        value = input("Geben Sie die gewünschte Temperatur ein: ")
                        self.controller.run_command(self.controller.devices[device_index], command, float(value))
                    elif "brightness" in command:
                        value = input("Geben Sie die Helligkeit (0-100) ein: ")
                        self.controller.run_command(self.controller.devices[device_index], command, int(value))
                    elif "color" in command:
                        value = input("Geben Sie die Farbe ein: ")
                        self.controller.run_command(self.controller.devices[device_index], command, value)
                    elif "resolution" in command:
                        value = input("Geben Sie die Auflösung ein: ")
                        self.controller.run_command(self.controller.devices[device_index], command, value)
                else:
                    self.controller.run_command(self.controller.devices[device_index], command)

        except KeyboardInterrupt:
            print("\n\033[1;31mProgramm beendet.\033[0m")