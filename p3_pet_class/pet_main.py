from pet_methods import Pet

def main():
    print("--- Testing Pet Class ---")
    
    my_pet = Pet()
    
    print("\nPlease enter your pet's details:")
    name_input = input("Name: ")
    type_input = input("Animal Type (e.g., Dog, Cat, Bird): ")
    age_input = input("Age: ")
    
    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)
    
    print("\n[Pet Details Stored in Object]")
    print(f"Pet Name: {my_pet.get_name()}")
    print(f"Pet Type: {my_pet.get_animal_type()}")
    print(f"Pet Age: {my_pet.get_age()}")

if __name__ == "__main__":
    main()
