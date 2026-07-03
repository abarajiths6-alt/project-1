from enum import Enum, auto
from dataclasses import dataclass
import random


class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return self.name.capitalize()


# Winning rules
WIN_RULES = {
    Choice.ROCK: Choice.SCISSORS,
    Choice.PAPER: Choice.ROCK,
    Choice.SCISSORS: Choice.PAPER
}


@dataclass
class Score:
    player: int = 0
    computer: int = 0
    ties: int = 0


class RockPaperScissors:
    def __init__(self):
        self.score = Score()

    def get_player_choice(self) -> Choice:
        while True:
            try:
                user = input("\nChoose (rock/paper/scissors): ").strip().upper()
                return Choice[user]
            except KeyError:
                print("❌ Invalid input! Try again.")

    @staticmethod
    def get_computer_choice() -> Choice:
        return random.choice(list(Choice))

    def determine_winner(self, player: Choice, computer: Choice) -> str:
        if player == computer:
            self.score.ties += 1
            return "🤝 It's a Tie!"

        if WIN_RULES[player] == computer:
            self.score.player += 1
            return "🎉 You Win!"

        self.score.computer += 1
        return "💻 Computer Wins!"

    def display_score(self):
        print("\n------ SCOREBOARD ------")
        print(f"Player   : {self.score.player}")
        print(f"Computer : {self.score.computer}")
        print(f"Ties     : {self.score.ties}")
        print("------------------------")

    def play(self):
        print("=" * 40)
        print("      ROCK PAPER SCISSORS")
        print("=" * 40)

        while True:
            player = self.get_player_choice()
            computer = self.get_computer_choice()

            print(f"\nYou      : {player}")
            print(f"Computer : {computer}")

            result = self.determine_winner(player, computer)
            print(result)

            self.display_score()

            again = input("\nPlay Again? (y/n): ").lower()
            if again != "y":
                print("\nFinal Score:")
                self.display_score()
                print("👋 Thanks for playing!")
                break


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()