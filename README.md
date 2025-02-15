# Collatz Conjecture Solving Algorithm
### by Václav (nymvaclav)

> The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. The conjecture has been shown to hold for all positive integers up to 2.95×1020, but no general proof has been found. - <a href="https://en.wikipedia.org/wiki/Collatz_conjecture">Wikipedia</a>


This is an algorithm I have created to prove the Collatz conjecture true or false. It tests each positive integer, and is hugely modifiable. You can select which integer to start from, how many integer do you want to check, at which integer do you want to stop, and which integer to exclude.

This Python program will create logs of all operations it did for each integer. You can disable the creation of logs at any time by running the setup.py file.

### To setup this program,
Run the setup.py file, which will ask questions like "which integer to start from?" or "which integer to exclude?". Your preferences will be saved into the preferences.json file.

### To start the algorithm,
Run the main.py file. This program will read the json file and adjust to fit your preferences, and then start calculating from the integer you wanted to start with. The program can by stopped at any time by simply closing the terminal, and it will use just one of your CPU's core. A program which will utilize all cores is still in development and will be out soon.

### Future changes?
I am planning to document how this program works in detail on my <a href="https://nymvaclav.github.io/">website</a>. Soon, I will release a version of this program that will utilize all of your CPU's cores.

### Can I see it in use?
Of course! Check the 'in-use' branch where you can find a video of this program being setup and running. You can also look through the logs, where you will find the calculations calculaten in the video.