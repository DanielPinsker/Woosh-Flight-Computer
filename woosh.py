
import colorama
from colorama import Fore
def newflight():
  print("<o>--~=~--<o>--~=~--<o>--~=~--<o>--~=~--<o>--~=~--<o>--~=~--<o>")
  print("")
  print("Welcome to the Woosh flight computer!")
  print("We'll ask you a few questions, and then model your flight!")
  print("On a scale of 1-5 (1 being smoothest), how smooth is your rocket?")
  smoothness = int(input(" "))
  print("What is the wind speed? (in Km/h)")
  windspeed = int(input(" "))
  print("How tall is the rocket? (in centimeters)")
  height = int(input(" "))
  print("What is the diameter of your rocket? (in centimeters)")
  width = int(input(" "))
  sidearea = height*(width * 0.25 * 3.14159) * 0.01
  print("How big are your rocket's fins? (square cm)")
  finsize = int(input(" "))
  print("How much does your rocket weigh, filled with fuel? (in kg)")
  loadedweight = int(input(" "))
  print("How much does your rocket weigh empty? (in kg)")
  emptyweight = int(input(" "))
  print("How many fins does your rocket have?")
  fincount = int(input(" "))
  upwardfacingarea = fincount * 0.001 + (width/1.5) * 3.14159
  print("How many kg's of thrust does your engine produce?")
  kgofthrust = int(input(" "))
  print("How much burntime does your engine provide in seconds?")
  burntime = int(input(" "))
  print(Fore.WHITE + "")
  print("~~~")
  print("Calculating...")
  print("~~~")
  print(Fore.WHITE + "")
  heightatburnout = (kgofthrust * 9.807)/((loadedweight + emptyweight)/2) * burntime - 9.82 * (burntime)
  print(Fore.GREEN + "Height at burnout: ",heightatburnout, " meters.")
  velocityatburnout = ((heightatburnout / burntime) * 1.3)
  print(Fore.GREEN + "Velocity at burnout:",velocityatburnout, " m/s.")
  airresistance = ((1.29 * 0.005 * smoothness  * upwardfacingarea)/2) * velocityatburnout/2
  calculatedheight = heightatburnout
  peakheight = 0
  time = 0
  newheight = 1
  oldheight = 0
  while (newheight > oldheight):  
    time = time + 1
    peakheight = calculatedheight
    calculatedheight = calculatedheight + velocityatburnout  - ((9.08 + (airresistance/emptyweight)) * time)
    newheight = calculatedheight
    oldheight = peakheight
  
  Gspulled = ((0 + velocityatburnout) / burntime)/9.81 
  print(Fore.GREEN + "G's Pulled:", Gspulled)
  
  
  print(Fore.GREEN + "Peak height: ", peakheight, " meters.")
  print(Fore.GREEN + "Reached peak at ", time + burntime, " seconds.") 
  print(Fore.GREEN + "Air resistance: ", airresistance, " Newtons.")
  print(Fore.GREEN + "Wobble:", ((windspeed * sidearea * 0.1 * (smoothness * 0.5)) / (finsize * fincount * 0.01))/(emptyweight * 0.01 + 1), "degrees max.")

 ## print(Fore.YELLOW + "")
  ##print("")
  ##print("""       .   -180km""", print("\/ - Rocket Here") if 179999 > peakheight > 175000 else print("."))
  ##print("""          """, print("\/ - Rocket Here") if 174999 > peakheight > 170000 else print("."))
  ##print("""          """, print("\/ - Rocket Here") if 169999 > peakheight > 165000 else print("."))
  ##print("""  .      """, print("\/ - Rocket Here") if 164999 > peakheight > 160000 else print("."))
  ##print("""           -160km""", print("\/ - Rocket Here") if 159999 > peakheight > 155000 else print("."))
  ##print("""        . """, print("\/ - Rocket Here") if 154999 > peakheight > 150000 else print("."))
  ##print(""".         """, print("\/ - Rocket Here") if 149999 > peakheight > 145000 else print("."))
  ##print("""          """, print("\/ - Rocket Here") if 144999 > peakheight > 140000 else print("."))
  ##print("""           -140km""", print("\/ - Rocket Here") if 139999 > peakheight > 135000 else print("."))
  ##print("""    .     """, print("\/ - Rocket Here") if 134999 > peakheight > 130000 else print("."))
  ##print("""          """, print("\/ - Rocket Here") if 129999 > peakheight > 125000 else print("."))
  ##print(""".       . """, print("\/ - Rocket Here") if 124999 > peakheight > 120000 else print("."))
  ##print("""           -120km""", print("\/ - Rocket Here") if 119999 > peakheight > 115000 else print("."))
  ##print("""      .   """, print("\/ - Rocket Here") if 114999 > peakheight > 110000 else print("."))
  ##print(""".         """, print("\/ - Rocket Here") if 109999 > peakheight > 105000 else print("."))
  ##print("""    .     """, print("\/ - Rocket Here") if 104999 > peakheight > 100000 else print("."))
  ##print(""".      .   -100km""", print("\/ - Rocket Here") if 99999 > peakheight > 95000 else print("."))
  ##print(""" .  .    .""", print("\/ - Rocket Here") if 94999 > peakheight > 90000 else print("."))
  ##print(Fore.BLUE +""".   .  .   -90km""", print("\/ - Rocket Here") if 89999 > peakheight > 85000 else print("."))
  ##print(""" . .  .  . """, print("\/ - Rocket Here") if 84999 > peakheight > 80000 else print("."))
  ##print(""" . . . . . -80km (Karman Line - Edge of space)""", print("\/ - Rocket Here") if 79999 > peakheight > 75000 else print("."))
  ##print(""". . . . .  """, print("\/ - Rocket Here") if 75999 > peakheight > 70000 else print("."))
  ##print(""".......... -70km""", print("\/ - Rocket Here") if 69999 > peakheight > 65000 else print("."))
  ##print(""",,,,,,,,,, """, print("\/ - Rocket Here") if 64999 > peakheight > 60000 else print("."))
  ##print("""********** -60km""", print("\/ - Rocket Here") if 59999 > peakheight > 55000 else print("."))
  ##print("""((""",Fore.WHITE +"""%%####""", print("\/ - Rocket Here") if 54999 > peakheight > 50000 else print("."))
  ##print(Fore.BLUE +"""(((""",Fore.WHITE +"""###""",Fore.BLUE +"""(( -50km""", print("\/ - Rocket Here") if 49999 > peakheight > 45000 else print("."))
  ##print("""//////////""", print("\/ - Rocket Here") if 44999 > peakheight > 40000 else print("."))
  ##print("""/""",Fore.WHITE +"""####""",Fore.BLUE +"""/// -40km""", print("\/ - Rocket Here") if 39999 > peakheight > 35000 else print("."))
  ##print("""//""",Fore.WHITE +"""##""",Fore.BLUE +"""////""", print("\/ - Rocket Here") if 34999 > peakheight > 30000 else print("."))
  ##print("""////////// -30km""", print("\/ - Rocket Here") if 29999 > peakheight > 25000 else print("."))
  ##print("""/////""",Fore.WHITE +"""####""",Fore.BLUE +""" """, print("\/ - Rocket Here") if 24999 > peakheight > 20000 else print("."))
  ##print("""//////""",Fore.WHITE +"""##""",Fore.BLUE +""" -20km """, print("\/ - Rocket Here") if 19999 > peakheight > 15000 else print("."))
  ##print("""////////// """, print("\/ - Rocket Here") if 9999 > peakheight > 5000 else print("."))
  ##print("""////////// -10km""", print("\/ - Rocket Here") if 14999 > peakheight > 10000 else print("."))
  ##print("""////////// """, print("\/ - Rocket Here") if 9999 > peakheight > 5000 else print("."))
  ##print("""////////// -0km""", print("\/ - Rocket Here") if 4999 > peakheight > 0 else print("."))
  ##print(Fore.GREEN +"""%#%#%#%#%#""")
  ##print("""**********""")
  print(Fore.WHITE + " ")


while (0 == 0):
  newflight()

##print("A") if a > b else print("B")
  
##(Ground temperature * atmospheric density at sea level + atmospheric density at 40km * temperature af 40 km + atmospheric density at 100km + amount over 100km)/(3) = atmospheric composition 

##(Wind speed at ground * wind speed 40km) * 0.613 * area in square meters * 1.2 (varies with smoothness) = wind force (newtons)

##Stability = speed * size of fins * rocket mass * wind force (measure speed of rotation and degrees of wobble)

##G's pulled = ((initial velocity - final velocity) / time spent accelerating)/9.81 

##Air resistance (In newtons) = ((atmospheric density * 0.02 (varies with smoothness) * square meters of upward facing spacecraft)/2)* velocity in meters per second 

##Measuring total height: height = height at burnout + velocity at burnout - air resistance/mass - gravity * time 

##Measuring height at burnout:
##Height (meters) = (Kg of thrust * 9.807)/((loadedweight + emptyweight)/2) * burn time (in seconds) - 9.82(burn time)

##Measuring velocity at burnout:
##(Height at burnout / burn time) * 1.5

#0. Initialize the rocket in a known position and orientation at time t = 0.

#1. Compute the local wind velocity and other atmospheric conditions.

#2. Compute the current airspeed, angle of attack, lateral wind direction and other flight parameters.

#3. Compute the aerodynamic forces and moments affecting the rocket.

#4. Compute the effect of motor thrust and gravity.

#5. Compute the mass and moments of inertia of the rocket and from these

#the linear and rotational acceleration of the rocket.

#6. Numerically integrate the acceleration to the rocket’s position and orientation during a time step ∆t and update the current time t 7→ t+∆t.

