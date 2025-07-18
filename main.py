from controller import SmartHomeController
from devices import Thermostat, SmartLight, SecurityCamera
from view import CLI

if __name__ == "__main__":

    # Create test devices
    td1 = Thermostat("Thermostat 1", ip_address="192.168.0.11")
    td2 = Thermostat("Thermostat 2", ip_address="192.168.0.12")
    td3 = SmartLight("Smarte Beleuchtung 1", ip_address="192.168.0.21")
    td4 = SmartLight("Smarte Beleuchtung 2", ip_address="192.168.0.22")
    td5 = SecurityCamera("Sicherheitskamera 1", ip_address="192.168.0.31")
    td6 = SecurityCamera("Sicherheitskamera 2", ip_address="192.168.0.32")

    # Initialize the Smart Home Controller
    controller = SmartHomeController()
    controller.add_device(td1)
    controller.add_device(td2)
    controller.add_device(td3)
    controller.add_device(td4)
    controller.add_device(td5)
    controller.add_device(td6)

    # Run the CLI
    cli = CLI(controller)
    cli.run()