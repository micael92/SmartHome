from controller import SmartHomeController
from devices import Device, Thermostat, SmartLight, SecurityCamera
from view import CLI

if __name__ == "__main__":

    # Initialize Smart Home Controller
    controller = SmartHomeController()

    # Example devices
    example_devices = [
        Device("Steckdose 1", ip_address="192.168.0.1"),
        Device("Steckdose 2", ip_address="192.168.0.2"),
        Device("Lüfter 1", ip_address="192.168.0.3"),
        Thermostat("Thermostat 1", ip_address="192.168.0.4"),
        Thermostat("Thermostat 2", ip_address="192.168.0.5"),
        SmartLight("Smarte Beleuchtung 1", ip_address="192.168.0.6"),
        SmartLight("Smarte Beleuchtung 2", ip_address="192.168.0.7"),
        SecurityCamera("Sicherheitskamera 1", ip_address="192.168.0.8"),
        SecurityCamera("Sicherheitskamera 2", ip_address="192.168.0.9"),
    ]

    # Add devices to controller
    for device in example_devices:
        controller.add_device(device)

    print(f"Smart Home Controller initialized {Device.get_device_count()} devices.")

    # Run the CLI
    cli = CLI(controller)
    cli.run()