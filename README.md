
-------------------------------------------------------------------------------------------------------

### Please note: I am first language is ISL (Irish Sign Language). I write in the second English language. I hope you read and understand the ReadMe

-------------------------------------------------------------------------------------------------------

## Concept Project

* The concept project for the Tic Tac Toe. The design function is very basic in Python.

* The project's development follows below:

## Flowchart

* Design for the functions:

<details>
<summary>See Flowchart click here</summary>
<img src="assets/images/Flowchart_Tic_Tac_Toe_part_1.jpg" alt=" design the flowchart for Tic Tac Toe">
<br>
<img src="assets/images/Flowchart_Tic_Tac_Toe_part_2.jpg" alt=" design the flowchart for Tic Tac Toe">
</details>

-------------------------------------------------------------------------------------------------------

# Design and development the Tic Tac Toe in Python

## Logo: Tic Tac Toe

- The logo head Tic Tac Toe, the font color is red and the background is white.
* When the user enters the name then The display shows up "Hello 'username' and 'Welcome to play Tic Tac Toe'.
* The rule is displayed to instruct how to play the game.

![CI logo](assets/images/Logo_welcome_rule.png)

Features
-------------

* The Tic Tac Toe have two players play turning between the computer and the human. The computer's player is 'o' and the human's player is 'x'.

![CI logo](assets/images/Project_3_mockup_responsive_screen.png)

Existing Features
-----------------------

### Start game

* <strong>The T.T.T begin game.</strong>
  * Please see the function as flowchart as seen above [Flowchart](#flowchart). I am putting the sections of the image to describe lists of how the player is beginning...

<details>
<summary><strong style="font-size:18px">See images sections click here</strong></summary>

## Ask the user to enter the name

<br>
  <img src="assets/images/Ask_user_name.png" alt="Screenshot show to ask the user enter the name before starting Tic Tac Toe game">
<br>

## Start game

<br>
  <img src="assets/images/Start_game.png" alt="Screenshot show begins the Tic Tac Toe game">
<br>

## Ask the user to press the number between 1 and 9

<br>

  <img src="assets/images/Press_number.png" alt="Screenshot show to ask the user entry pick the numbers">
<br>

## The human player's winner by 'x'

<br>

  <img src="assets/images/Ask_play_again.png" alt="Screenshot show who is winner by 'x'">
<br>

## The computer player's winner by 'o'

<br>

  <img src="assets/images/Computer_winner.png" alt="Screenshot show who is winner by 'o'">
<br>

## The tie

<br>

  <img src="assets/images/Problem_tie.png" alt="Screenshot show the tie!">
<br>

## Ask the user to play again either typing 'yes' or 'no'

<br>

  <img src="assets/images/Ask_play_again.png" alt="Screenshot show to ask the user entry yes or no">
<br>

## The human player types "yes" then the computer's player will start at the first and then turn the human player to continue

<br>

  <img src="assets/images/Turn_Computer_player.png" alt="Screenshot show to ask user type 'yes' or 'no'">
<br>

## Error handlers

* Over 9 numbers show up as an error

  <img src="assets/images/Error_over_9.png" alt="Screenshot show, the error handle to ask user to use number between 1 and 9">

* letter error, to ask the user to enter the number between 1 and 9

  <img src="assets/images/Error_letter.png" alt="Screenshot show, the error handle to ask user to use number between 1 and 9">

* Error shows up the player takes either 'x' or 'o'

  <img src="assets/images/Player_taken.png" alt="Screenshot show, the error handler to ask the user that the player have taken">

* Error shows up, ask the user to type 'yes' or 'no'

  <img src="assets/images/Error_yes_or_no.png" alt="Screenshot show, the error handler to ask a user to type 'yes' or 'no'">

## Ask the user, the human player type 'no' and the display show up to say "Goodbye! Come back to play again :)"

<br>

  <img src="assets/images/End_game.png" alt="Screenshot show, the user type 'no' to say 'Goodbye!, Come back to play again'">
<br>

</details>

## Testing

### The browser compatibility

* The testing runs for Chrome, Opera, Microsoft Edge, Safari and Firefox for the Heroku app. I found Chrome, Opera and Microsoft Edge, it does not great visual while you are playing a game. I would not recommend using those.

* I am finding Safari and Firefox, it does very clear visuals while playing. I would recommend using Safari or Firefox.

### The devices

* I was testing on my iPhone and seem it does not work at all but my mentor Rory does work on his mobile device.

### The test running game in Heroku app

* Almost the function works except the check_draw does not work because I want to see the prompt "it's tie on the screen when it was tie.

* It was working before when I asked the tutor because I found it have some glitches and I want to solve check_draw. we tried to figure out what was the problem. Unfortunately, my time allowance was hit up. I ran to fix it several times and could not find a solution. My deadline was so closed then I stop to fix it and move on to do ReadMe.

## Validation testing

* [The CI Python Linter](https://pep8ci.herokuapp.com/#) had been running testing and there are lots of errors and fixing the bugs. Now there are no errors.

<details>
<summary><strong style="font-size:18px">See images sections click here</strong></summary>

## lot of the errors

<br>
  <img src="assets/images/Show_Errors_CI_Python_liner.png" alt="Screenshot show the website called 'CI Python linter, display a lot of errors">
<br>

## Last Error

<br>
  <img src="assets/images/Last_Error_CI_Python_liner.png" alt="Screenshot show the website called 'CI Python linter, less the errors">
<br>

## No Error

<br>

  <img src="assets/images/No_Error_CI_liner.png" alt="Screenshot show the website called 'CI Python linter, all clear the errors">
<br>

</details>

# Deployment

[The Heroku app page](https://www.heroku.com/) where is deployed. How do processing the site deployed as follows:

* Login
* use the Google Authenticator app and open the screen display of the code number
and Verify Your Identity page "Verification Code" and insert the code in the box
then click on Verify button.
* Click on the button "Create new app"
* Type in the box "project-3-robert-quinlan"
* Select Europe
* Click on the "Create app" button
* To click "project-3-robert-quinlan" to open
* Click on "Deploy" on the top menu
* On RQISL next to the box copy from GitHub <https://github.com/RQISL/portfolio-project-3-robert-quinlan> to paste onto the box then click on to "search" button
* prompt shows the link active then click on the "connect" button
* Make sure to check the "Enable Automatic" button is on
* click on the "Deploy Branch" button
* Prompts active on the screen until the completed
* Click on the "View" button to open the page
* I would <strong>recommend</strong> to use Safari or Firefox browser compatibility

### The deployed site is now live [Tic Tac Toe](https://project-3-robert-quinlan.herokuapp.com/)

## Credits

I learned very new to me use Python. I enjoyed creating the Tic Tac Toe in Python.

The Tutors team was great support and encourage me to developed learning to use Python.

My mentor had good feedback and helps with my process improvement on the site project.

## Resouce & tutorial

* ### I learned as many resources as possible I could learn how use create the Tic Tac Toe game in Python

### Example Flowchat to help me design the flowchart as see [Flowchart](#flowchart) above

1) <https://www.programiz.com/article/flowchart-programming>
2) <https://problemsolvingwithpython.com/08-If-Else-Try-Except/08.06-Flowcharts/>

### Tic Tac Toe tutorials, help me to concept how I create the coding in Python

1) <https://www.youtube.com/watch?v=dK6gJw4-NCo&t=32s>
2) <https://www.youtube.com/watch?v=M3G1ZgOMFxo>
3) <https://medium.com/@estebanthi/tic-tac-toe-game-in-python-for-beginners-6c09bb63eb84>
4) <https://www.javatpoint.com/tic-tac-toe-in-python>
5) <https://www.youtube.com/watch?v=BHh654_7Cmw>
6) <https://www.youtube.com/watch?v=n2o8ckO-lfk>

### Color, I choose these for my project and I want to learn various syntaxes for the color option to use

1) <https://pypi.org/project/colored/>
2) <https://www.geeksforgeeks.org/print-colors-python-terminal/>
3) <https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python#google_vignette>
4) <https://pypi.org/project/colorama/>

### Error Handles tutorials, helps me to see how can I create the error handle

1) <https://www.freecodecamp.org/news/how-to-handle-errors-in-python/>
2) <https://www.geeksforgeeks.org/handling-nameerror-exception-in-python/>
3) <https://www.w3schools.com/python/python_try_except.asp>  

## Technologies Used

1) [Code Anywhere](https://app.codeanywhere.com/) - Active development in Python
2) [The CI Python Linter](https://pep8ci.herokuapp.com/#) - Run testing any errors to fix the bugs
3) [Heroku app](https://www.heroku.com/) - The deployed to active the browser. My project is completed and now live [Tic Tac Toe](https://project-3-robert-quinlan.herokuapp.com/)

## Concluded

* I completed my concept project for the Tic Tac Toe. I created very basic Python. The site lives [Tic Tac Toe](https://project-3-robert-quinlan.herokuapp.com/)
