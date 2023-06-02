import random

def roll_dice():
  """Rolls a pair of dice and returns the sum of the results."""
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  return die1 + die2

def main():
  """The main function of the program."""
  while True:
    roll = roll_dice()
    print("You rolled a", roll)

    # Check if the user wants to roll again.
    again = input("Roll again? (y/n): ")
    if again == "n":
      break

if __name__ == "__main__":
  main()