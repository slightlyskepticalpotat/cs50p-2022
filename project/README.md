# file-visualiser

### Video Demo: https://youtu.be/KDAWuAjN6tY
### Description:

In short, my project turns any computer file (as long as it fits within the program memory) into an image. I initially thought of this idea because I knew different files had different patterns of binary data. What if we could display those patterns? Of the five senses I thought touch, smell, and taste were impossible to achieve with a computer program, and I couldn't think of a clean mapping from individual bits and bytes to audio waves. Therefore, I settled on sight.

The program is divided into three major parts, all encapsulated with the principles of OOP. The first part gets the file and processes it into an array of bytes. The second part takes that array and turns it into an image. Finally, the third part saves it. My program is very extensible because the first and second parts can easily be swapped out with different functions, perhaps specified by the user with command-line options. Of my dependencies, pillow is used to actually generate the image and pytest is used to run my test suite.

Some ideas I have for extension include processing the file differently (taking difference between bytes, taking every nth byte, or seeding a random number generator instead of taking the raw bytes) and rendering the file differently (colour instead of black and white, transparency, animation).

When running the program, I noticed that different files sometimes gave distinctive patterns. For example, a file with 256 ascending bytes gave a 16x16 pixel grid of shades. A rainbow flag gave six black and white stripes, and english text gave a largely gray field (as letters have similar byte values). My code is available through the project submission.

You can run the program with python project.py. It will ask you to enter an input image path, process the image, and then enter an output image path.