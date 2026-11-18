def calculate_molarity(moles, volume_liters):return moles / volume_liters
def main(): 
    compound = input ("Enter the name of the compound: ")
    moles = float(input("Enter moles (mol): "))
    volume_ml = float(input("Enter volume (mL): "))

    volume_liters = volume_ml / 1000
    molarity = calculate_molarity(moles, volume_liters)

    print(f"The concentration of {compound} is {molarity:.3f} M.")
main()