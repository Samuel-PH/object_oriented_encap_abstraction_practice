from fan_methods import Fan

def main():
    print("--- Testing Fan Class ---")
    
    fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
    
    fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)

    print("\n[Object 1 Properties]")
    fan1.display_status()
    
    print("\n[Object 2 Properties]")
    fan2.display_status()

if __name__ == "__main__":
    main()

