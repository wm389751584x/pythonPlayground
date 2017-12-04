def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet(pet_name='willie', animal_type='cat') # passing the argument as "name, value" so there is no confusing.