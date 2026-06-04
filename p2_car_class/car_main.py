from car_methods import Car

def main():
    print("--- Testing Car Class ---")
    
    my_car = Car(year_model=2024, make="Porsche")
    
    print("\n[Accelerating...]")
    for i in range(1, 6):
        my_car.accelerate()
        print(f"Time {i}: Current speed is {my_car.get_speed()} mph")
        
    print("\n[Braking...]")
    for i in range(1, 6):
        my_car.brake()
        print(f"Time {i}: Current speed is {my_car.get_speed()} mph")

if __name__ == "__main__":
    main()