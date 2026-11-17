# Typing-speed-tester
A command line based typing speed tester developed using python
# Python Typing Speed Test

A simple command-line Typing Speed Test application developed using Python. It measures the user's typing speed in Words Per Minute (WPM) and calculates typing accuracy based on a randomly selected paragraph.

## Features

- **Random Paragraph Generation:** Displays a randomly selected paragraph from a collection of five texts.
- **Typing Speed Calculation:** Measures typing speed in Words Per Minute (WPM).
- **Accuracy Measurement:** Calculates typing accuracy by comparing the entered text with the original paragraph.
- **Time Tracking:** Records the total time taken to type the paragraph.
- **Simple Interface:** Easy-to-use command-line interface.

## Technologies Used

- Python 3
- `time` module
- `random` module

## How It Works

1. The program randomly selects a paragraph from a predefined collection.
2. The selected paragraph is displayed on the screen.
3. The user presses Enter to start typing.
4. The program records the typing time.
5. After submission, it calculates:
   - **Typing Speed (WPM):** Number of words typed divided by the time taken in minutes.
   - **Accuracy (%):** Percentage of correctly matched characters compared with the original paragraph.
6. Finally, it displays the typing speed, accuracy, and total time taken.

## Installation and Execution

**1. Clone the repository**


git clone https://github.com/koushikk2005/Typing-speed-tester.git


**2. Navigate to the project directory**

```bash
cd REPOSITORY_NAME
```

**3. Run the Python file**

```bash
python main.py
```

## Sample Output

```text
Early morning is often the most peaceful time of the day...

Write the text showing above press 'Enter' to start typing:
=> Early morning is often the most peaceful time...

your typing speed is 45 words per min and accuracy is 95.50%

You typed the above text in 32.45 seconds
```

*Note: Sample output is illustrative.*

## Future Improvements

- Add a graphical user interface (GUI).
- Include multiple difficulty levels.
- Display typing progress in real time.
- Maintain a history of typing test results.
- Add a leaderboard to track high scores.
- Improve accuracy calculation to handle extra and missing characters.

## Author

**Koushik Khan**

A Python project developed to practice programming fundamentals, functions, loops, string operations, and time-based calculations.

---

⭐ If you find this project useful, consider giving the repository a star!
