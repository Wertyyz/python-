def ryan():
    password = raw_input("PASSWORD: ").lower()
    if password == "fs15rocks":
        print "Welcome!"
        run = raw_input("What would you like to do?").lower()
        if run == "game":
            print "Welcome To My Game!"
            print "Would you like to play?"
            play = raw_input("Type Play to play. ").lower()
            if play == "play":
                print "Let's get started!"
                print "In this game, you will be a cashier at a grocery store."
                print "Story"
                print "You are wanting a job. You see that Ryan’s Grocery has a job opening as cashier.  You go in and fill in an application.  The next day, you get a call saying you got the job and that your first day is Monday."
                print "Your pay is $9 per hour."
                print "The First Day"
                print "Your first customer is a older man.  He is buying a dozen eggs.  The price is $1.40.  The man pays $2.00.  What is his change?"
                first_change = raw_input("Type the correct amount of change.  \(blank cents\) ").lower()
                if first_change == "60 cents":
                    print "That is correct."
                    print "The next customer is buying a gallon of milk for $2.50 and 12 eggs for $1.40.  How much should they pay?"
                    first_payment = raw_input("Type the correct amount.  \($blank\) ").lower()
                    if first_payment == "$3.90":
                        print "Good job"
                        print "You next customer is buying beer.  You are 20 years old.  To get someone who can handle the beer, call extension 1905."
                        call_one = raw_input("Type 1905 to call. ").lower()
                        if call_one == "1905":
                            print "A man answers.  He asks what aisle you are in.  You are in aisle 7."
                            aisle =  raw_input("Type \"7\" ").lower()
                            if aisle == "7":
                                print "The man says he is on his way."
                                print "The man comes and checks out the beer.  The customer's bill is $23.00.  Tell the customer their bill."
                                bill_one = raw_input("Type the bill of $23.00 ").lower()
                                if bill_one == "$23.00" or "$23" or "23.00":
                                    print "Customer pays and leaves."
                                    print "the next customer has arrived.  They need you to price check an item.  The computer says the item is $5.00.  Tell the customer the price."
                                    price_one = raw_input("Type the amount. ").lower()
                                    if price_one == "$5.00" or "$5" or "5.00":
                                        print "Customer says \"Thanks\" and leaves."
                                        print "Your last customer of the day has arrived.  He is getting a gallon of milk for $2.50, a dozen eggs for $1.40, and a 4 pack of cookies for $1.00."
                                        tell_1 = raw_input("Tell the customer the bill. ").lower()
                                        if tell_1 == "$4.90" or 4.90:
                                            print "Customer pays and leaves."
                                            print "Your total is $9."
                                    else:
                                        print "That is not correct"
            
                    else:
                        print "That is incorrect."
                else:
                    print "That is not correct."  
            else:
                print "You did not type Play!"
        if run == "math":
            import random
            random = random.randrange(10)
            while 10 > 9:
                print random + "x" + random
                prob = raw_input("Type Answer. ").lower() 
        if run == "calculator":
            def add():
                print "Enter the two numbers to Add"
                A=int(raw_input("Enter A: "))
                B=int(raw_input("Enter B: "))
                return A + B 


            def sub():
                print "Enter the two numbers to Subtract"
                A=int(raw_input("Enter A: "))
                B=int(raw_input("Enter B: "))
                return A - B


            def mul():
                print "Enter the two numbers to Multiply"
                A=int(raw_input("Enter A: "))
                B=int(raw_input("Enter B: "))
                return A * B


            def div():
                print "Enter the two number to Divide"
                A=float(raw_input("Enter A: "))
                B=float(raw_input("Enter B: "))
                return A / B


            print "1: ADDITION"
            print "2: SUBTRACTION"
            print "3: MULTIPLICATION"
            print "4: DIVITION"
            print "0: QUIT"


            while True:


                CHOICE = int(raw_input("ENTER THE CORRESPONDING NUMBER FOR CALCULATION ")) 


                if CHOICE == 1: 
                    print 'ADDING TWO NUMBERS:'
                    print add()


                elif CHOICE == 2:
                    print 'SUBTRACTING TWO NUMBERS'
                    print sub()


                elif CHOICE == 3:
                    print 'MULTIPLYING TWO NUMBERS'
                    print mul()


                elif CHOICE == 4:
                    print "DIVIDING TWO NUMBERS"
                    print div()


                elif CHOICE == 0:
                    exit()
                else:
                    print "The value Enter value from 1-4"
        if run == "randomnum":
            import random
            end = raw_input("Type highest random number.").lower()
            stop = random.randrange(int(end))
            print stop
        if run == "randomword":
            import random    
            hi = raw_input("Type List of words.")
            words = hi
            word = random.choice(words)
            print word
        if run == "games":
            print "Slither.io"
            print "Diep.io"
            print "Roblox.com"
            print "Splix.io"
            print "Agar.io"
            print "For Agar.io private server, go to github.org/ProjectOgar/Ogar.  Then, run \and go to agar.io/ip?/127.0.0.1"
        if run == "game1":
            print "You have chosen to play the second game."
            print "In this game, you will design things."
            while True: 
                print "Would you like to design a shoe, blanket, shirt, pants, or a hat?"
                answer1 = raw_input("Type your answer.").lower
                if answer1 == "shoe":
                    print "You have chosen to design a shoe."
                    print "Let's get started."
                    print 