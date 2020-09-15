print("Welcome to my python game!")
name = input("what is your name? ")
age = int(input("what is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10



if age >= 18:
    print("You are old enough")

    weapon = input("Pick a weapon (sword/basebat)")

    wants_to_play = input("Do you want to play?").lower()
    if wants_to_play == "yes":
        print ("You start with",health , "health" )
        print("Play game!")

        left_or_right = input("First choice......Left or Right (left/right)?")
        if left_or_right == "right":
            ans = input("Great, follow the path and reach a lake.... Do you swm across or go around(across/around)? ")

            if ans == "around":
                print("you went around and reached the other side of the lake.")
            
            elif ans == "across":
                print("You got across the lake but were bit by a shark and lost health.")
                health -=5

            ans = input("You notice a house and a river which one do you choose (river/house)? ")
            if ans == "house":
                print("You go to the house and see the owner, he doesnt like and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived the game  You win!!")

            else:
                print("You fell in the river and lost...")

        else:
            print("Yoe fell down and lost...")

    else:
        print("bye...")



else:
    print("You are not old enough to play the game")

#remainder/modulus %