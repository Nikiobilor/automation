train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
      c_temp = f_temp - 32 * 5/9
        return c_temp
    f100_in_celsius = f_to_c(100)
    def c_to_f(c_temp):
          f_temp = c_temp * 9/5 + 32
            return f_temp
        c0_in_fahrenheit = c_to_f(0)
        print(c0_in_fahrenheit, ' fahrenheit')
        print(f100_in_celsius, ' celsius')

        def get_force(mass, acceleration):
              return mass*acceleration
          #the return statement is what does the calculation or what you need the parameters in the function to do,so when you call the function, mass gets assigned the value of train_mass and acceleration the value of train_acceleration.
          train_force = get_force(train_mass, train_acceleration)
          #therefore value of train_force is the product of the statement in line 21 i.e mass*acceleration
          print (train_force)
          print('The GE train supplies,', train_force,' Newtons of force')
          def get_energy(mass, c):
                return mass * c**2
            #the return statement is what does the calculation or what you need the parameters in the function to do,so when you call the function, mass gets assigned the value of bomb_mass and c the value of c.
            bomb_energy = get_energy(bomb_mass, c = 3*10**8)
            #therefore value of bomb_energy is the product of the statement in line 28 i.e mass*c**2
            print(bomb_energy)
            print('A 1kg bomb supplies', bomb_energy, ' Joules')
            def get_work(mass, acceleration, distance):
                  work = get_force(mass, acceleration)
                  #line 35 takes its value from line 21 and returns the product of line 21
                    return work*distance
                train_work = get_work(train_mass, train_acceleration, train_distance)
                print(train_work)
                print('The GE train does',  train_work, 'Joules of work over', train_distance, 'meters')




    #Answers

     32.0  fahrenheit
     82.22222222222223  celsius
     226800
     The GE train supplies, 226800  Newtons of force
     90000000000000000
     A 1kg bomb supplies 90000000000000000  Joules
     22680000
     The GE train does 22680000 Joules of work over 100 meters
