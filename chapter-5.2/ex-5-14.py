# Programming Exercise 5-14
#
# Program to compute kinetic energy from mass and velocity.
# This program accepts values for mass and velocity from the user in kilograms and meters per second,
# passes them to a function that returns kinetic energy in joules calculated from those values,
# and displays the result.


# define the main function
def main():
    # define local float variables for mass, velocity and kinetic energy
    mass = 0.0
    velocity = 0.0

    # Get mass from user
    mass = int(input("Mass in kilograms: "))

    # Get velocity from user
    velocity = int(input("Velocity in meters per second: "))

    # Get kinetic energy in joules from the kinetic energy function
    kinetic_energy(mass, velocity)
    ke = kinetic_energy(mass, velocity)
    print("Kinetic energy in joules: ", format(ke, '.2f'))
    
    # Display kinetic energy in joules, formatted to 2 decimal places.



# Define a function to calculate kinetic energy in joules.
# The function accepts two parameters, mass in kilograms and velocity in meters/second,
# uses a formula to calculate the joules of kinetic energy,
# and returns the result
def kinetic_energy(mass, velocity):
    ke = 0.5*mass*(velocity**2)
    return ke
    # Define a local variable for joules of kinetic energy

	# calculate the kinetic energy using the parameters and the conversion formula    

	# return the result



# Call the main function to start the program
main()


