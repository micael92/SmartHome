from controller import SmartHomeController
from devices import Device, Thermostat, SmartLight, SecurityCamera
from view import CLI

if __name__ == "__main__":

    # Initialize Smart Home Controller
    controller = SmartHomeController()

    # Add devices to controller
    controller.add_device(Device("Steckdose 1", ip_address="192.168.0.1"))
    controller.add_device(Device("Steckdose 2", ip_address="192.168.0.2"))
    controller.add_device(Device("Lüfter 1", ip_address="192.168.0.3"))
    controller.add_device(Thermostat("Thermostat 1", ip_address="192.168.0.11"))
    controller.add_device(Thermostat("Thermostat 2", ip_address="192.168.0.12"))
    controller.add_device(SmartLight("Smarte Beleuchtung 1", ip_address="192.168.0.21"))
    controller.add_device(SmartLight("Smarte Beleuchtung 2", ip_address="192.168.0.22"))
    controller.add_device(SecurityCamera("Sicherheitskamera 1", ip_address="192.168.0.31"))
    controller.add_device(SecurityCamera("Sicherheitskamera 2", ip_address="192.168.0.32"))

    print(f"Smart Home Controller initialized {Device.get_device_count()} devices.")

    # Run the CLI
    cli = CLI(controller)
    cli.run()