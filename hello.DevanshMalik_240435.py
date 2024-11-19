# Importing necessary libraries
import sys

def main():
    input_count = int(input("Enter the amount of strings to input: "))
    strings = []

    print(f"\nEnter {input_count} strings:")
    for _ in range(input_count):
        strings.append(input())

    # Sorting the strings
    strings.sort()

    print("\nSorted Strings:")
    for string in strings:
        print(string)

if __name__ == "__main__":
    main()

