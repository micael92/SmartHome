class SmartHomeController:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print("Device added:", device.name)

    def remove_device(self, device):
        self.devices.remove(device)
        print("Device removed:", device.name)

    def list_devices(self):
        return [device.name for device in self.devices]
    
    def run_command(self, device, command, *args):

        print(f"Running command '{command}' on device '{device.name}'")

        if command == "turn_on":
            device.turn_on()
        elif command == "turn_off":
            device.turn_off()
        elif command == "get_status":
            print(f"{device.name}'s Status is {device.get_status()}")
        elif command == "get_actual_temp":
            return device.get_actual_temp()
        elif command == "set_target_temp":
            return device.set_target_temp(args[0])
        
        elif command == "set_brightness":
            return device.set_brightness(args[0])
        elif command == "set_color":
            return device.set_color(args[0])
        
        elif command == "set_resolution":
            return device.set_resolution(args[0])
        elif command == "start_recording":
            return device.start_recording()
        elif command == "stop_recording":
            return device.stop_recording()
        elif command == "set_ip_address":
            return device.set_ip_address(args[0])
    
        else:
            return f"Invalid command for Device {device.name}"
        
    