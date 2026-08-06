# CP1404 Assignment 2: Album Archive 2.0 by YOURNAME


## 1. How many hours did you spend working on this assignment 2 project?

The entire project took me approximately eight hours to complete. This included designing the classes, writing and testing the console program, building the Kivy GUI, debugging problems, and completing the documentation.

## 2. What are you most satisfied with?

I am most satisfied with the separation between the data classes and the user interfaces. The Album and AlbumCollection classes contain the core data and collection logic, while the console and Kivy programs handle user interaction separately. This allowed me to reuse the same classes in both versions of the application. I am also satisfied that the GUI dynamically creates colour-coded buttons for the albums and updates the number of required albums whenever their status changes.

## 3. What are you least satisfied with?

I am least satisfied with the visual design of the GUI. Although it is functional and easy to understand, it is still quite simple and could be made more polished. For example, the spacing, colours, button styles, and resizing behaviour could be improved. The tests are also based on simple assertions rather than a more structured testing framework, so they could cover more edge cases and provide clearer information when a test fails.

## 4. What worked well in your development process?

Developing the Album and AlbumCollection classes before building the user interfaces worked well. It allowed me to test the main program logic independently before connecting it to the console and GUI programs. Breaking the project into smaller parts also made errors easier to locate. Testing methods such as sorting, loading, saving, and changing album status helped me confirm that the core behaviour was correct before I worked on the interface.

Using small functions and methods with specific responsibilities also worked well. This kept the code easier to read and reduced unnecessary repetition. Making small Git commits after meaningful changes would also make the development history easier to understand and help identify when a problem was introduced.



## 5. What about your process could be improved the next time you do a project like this?

Next time, I would create a clearer plan before starting the implementation. I would list the required features, decide which class or function should be responsible for each feature, and identify the tests needed for each part. This would reduce the need to change the program structure later.

I would also test the GUI more frequently while developing it instead of waiting until most of the interface was complete. In addition, I would write more edge-case tests, such as loading an empty file, handling invalid JSON data, sorting albums with identical values, and checking invalid user input. I would also commit changes more regularly with clear, imperative commit messages.

## 6. Describe what learning resources you used and how you used them.

I used the CP1404 lecture materials, practical exercises, assignment instructions, and examples from previous practical tasks. The course materials helped me review object-oriented programming, class design, file handling, exception handling, constants, and clean-code conventions.

I also used the official Python documentation to confirm how JSON file handling, pathlib, sorting, and exceptions work. For the GUI, I referred to Kivy documentation and examples to understand KV language layouts, widget IDs, event handlers, dynamic buttons, colours, sizing, and scrolling. I used these resources to understand the required concepts and then adapted the examples to suit the structure of my own program.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

One of the main challenges was keeping the console program and GUI program consistent while avoiding duplicated data logic. I overcame this by placing the shared behaviour in the Album and AlbumCollection classes and using those classes in both programs.

Another challenge was dynamically displaying albums in the Kivy interface. Each album needed its own button, colour, status-changing behaviour, and connection to the correct Album object. I solved this by creating the buttons in display_albums, storing the related album on each button, and binding every button to the same handler method.

Input validation and sorting also required careful handling. I used try and except to validate the year, checked for empty fields before adding an album, and mapped the text shown in the sorting spinner to the correct album attribute. Testing each part separately helped me find and fix problems before combining all the features.

