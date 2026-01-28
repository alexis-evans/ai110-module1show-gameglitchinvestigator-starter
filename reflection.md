# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The game was a simple Streamlit app that had a title, a message indicating I should guess a number between 1 and 100, displaying that I had 7 attempts left, with buttons to submit my guess after I type it in the text box, start a new game, and a checkbox to indicate if I wanted to show hints or not which defaulted to yes. It also had a sidebar that allowed me to set my difficulty (Easy, Normal, or Hard), showed me the range that the secret number would (should) be in, and how many attempts I was allowed.

Bugs that I noticed immediately is that the hints would tell me to go in the opposite direction of the actual secret number, my attempts didn't go down when I hit submit guess, but when I guessed my next number (which is a little weird), the new game button doesn't reset the game just the secret number but you can't actually play twice in a row, and the game without the hints is kind of impossible, so not sure why it's even an option to begin with. Also, the amount of guesses starts at 7 initially, but when you hit new game it resets to 8.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used the Copilot agent within VS Code. I always provided context (when I remembered) by using the files that held the code I was working on as inputs to my prompt. I didn't really use session hygiene as much because I tend to always work in one chat so that the AI can remember things about formatting and variable names and other things like that so I don't have to repeat myself as much. I also just don't really like switching between chats if I'm talking about the same project. One AI suggestion that I accepted was the changing of the hints to the right direction. The change was simple so it was easy to verify that it was correct, so I accepted it. One AI suggestion I rejected was the initial test cases it wrote to verify the new game button worked. I realized that the test cases weren't actually checking if the button worked, but rather manually resetting the variables for the different game states and asserting that they were changed correctly. I brought this up to the agent, and it recommended creating a new function called reset_game_state() that was called when the new game button was pressed, so that way we can test the function is working correctly. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when I tested it myself on the app. Just the tests passing wasn't enough. So I would go into the app and start from different states to make sure my fixes worked as intented. One manual test I ran was the New Game button. I wanted to make sure that it really reset the game state, so I tried it both when I was in the middle of an ongoing game and when I had won and lost a game. It showed me that the button actually worked, and that the test cases that I wrote with AI were correct. Copilot helped me write all my new unit tests. I would tell it that I wanted to test a certain fix that I implemented, and it would write a test for me. Then, I would verify that the test seemed to be doing what I wanted it to do, and if not, I would iterate with the agent until it created something that I was happy with.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

I did not experience the secret number changing during a game. I only noticed it when I would hit the "New Game" button and the secret number would change but none of the other variables would reset for a new game to start. I would explain a rerun as having to manually reset session state variables to their "default" values because Streamlit can't do it automatically for you. You have to explicitly tell it what values are default because it doesn't know on its own. The change I made that solved the problem was fixing the New Game button to reset not only the secret number, but also return the attempts and score states to 0 and clearing the history to an empty dictionary.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I would like to use the Agent more because it seems to work fairly well and I can still check the code it's writing to make sure it's what I want. I suppose I should also get into the habit of writing unit tests, because usually I just test it myself, but the unit test can catch things easier than I can in some instances and save me time. Something I would do differently is not accepting suggestions blindly because they seem correct on the surface level. Like for the initial test for the "New Game" button, the test would have passed and the button would have worked, but had I not looked at the test, I wouldn't have known that those were two separate occurences and that the test wasn't actually testing the button at all. This project made me feel that AI has great coding potential, but it's not perfect yet, so it's still important to go behind it and check its work.
