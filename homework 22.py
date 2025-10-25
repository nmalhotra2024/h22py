class Reverse:
    def __init__(self, text=""):
        self.text = text

    def get_reversed(self):
        """Return the reversed version of the text."""
        return self.text[::-1]
    
    from reverse import Reverse

def main():
    # Take input from the user
    user_input = input("Enter a word to reverse: ")

    # Create Reverse object with user input
    rev = Reverse(user_input)

    # Display reversed string
    print("Reversed word:", rev.get_reversed())

if __name__ == "__main__":
    main()