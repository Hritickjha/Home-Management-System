class HomeManagementSystem:
    
    def __init__(self):
        self.lights_status = False
        self.temperature = 22  # initial temperature in celsius
        self.alarm_status = False
        
    def main_menu(self):
        print("\nHome Management System")
        print("1. Control Lights")
        print("2. Adjust Thermostat")
        print("3. Control Security System")
        print("4. View Status")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        return choice
    
    def lights_menu(self):
        print("\nControl Lights")
        print("1. Turn on Lights")
        print("2. Turn off Lights")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice (1-3): ")
        return choice
    
    def thermostat_menu(self):
        print("\nAdjust Thermostat")
        print("1. Increase Temperature")
        print("2. Decrease Temperature")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice (1-3): ")
        return choice
    
    def security_menu(self):
        print("\nControl Security System")
        print("1. Arm Alarm")
        print("2. Disarm Alarm")
        print("3. Back to Main Menu")  
        
        choice = input("Enter your choice (1-3): ")
        return choice
    
    def view_status(self):
        print("\nCurrent Status:")
        print(f"Lights: {'On' if self.lights_status else 'Off'}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Security System: {'Armed' if self.alarm_status else 'Disarmed'}")
    
    def control_lights(self):
        while True:
            choice = self.lights_menu()
            
            if choice == "1":
                self.lights_status = True
                print("Lights turned on.")
            elif choice == "2":
                self.lights_status = False
                print("Lights turned off.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def adjust_temperature(self):
        while True:
            choice = self.thermostat_menu()
            
            if choice == "1":
                self.temperature += 1
                print(f"Temperature increased to {self.temperature}°C")
            elif choice == "2":
                self.temperature -= 1
                print(f"Temperature decreased to {self.temperature}°C")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def control_security(self):
        while True:
            choice = self.security_menu()
            
            if choice == "1":
                self.alarm_status = True
                print("Security System armed.")
            elif choice == "2":
                self.alarm_status = False
                print("Security System disarmed.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
                
    def run(self):
        while True:
            choice = self.main_menu()
            
            if choice == "1":
                self.control_lights()
            elif choice == "2":
                self.adjust_temperature()
            elif choice == "3":
                self.control_security()
            elif choice == "4":
                self.view_status()
            elif choice == "5":
                print("Exiting the Home Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    system = HomeManagementSystem()
    system.run()

            
        
        