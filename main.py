import dice
import score

def main():
    while True:
        print("\n1.Play 2.Score 3.Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            player = dice.roll()
            computer = dice.roll()

            print("You:", player)
            print("Computer:", computer)

            if player > computer:
                print("You win")
                score.save("Player")
            elif computer > player:
                print("Computer wins")
                score.save("Computer")
            else:
                print("Draw")
                score.save("Draw")

        elif choice == '2':
            print(score.get())

        elif choice == '3':
            break

if __name__ == "__main__":
    main()