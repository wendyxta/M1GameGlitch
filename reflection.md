# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

Secret: 53
| Input | Expected Behavior | Actual Behavior | Console Output / Error        |
|-------|-------------------|-----------------|-------------------------------|
|80     |go lower           |go higher        |incorrect higher/lower hint    |
|95     |go lower           |go higher        |incorrect higher/lower         |
|105    |go lower           |go higher        |allow answer past range 1-100  |
|13     |go higher          |go lower         |incorrect higher/lower         |
|-23    |go higher          |go lower         |allow answer below range 1-100 |
|53     |correct (+5)       |correct (-5)     |lost points for correct answer |
|13     |correct            |correct          |(1st try correct) --> score box doesnt update even though console says final score: 70
error: new game doesnt work after winning a game, secret changes, but history stays, and console message "You already won. Start a new game to play again."
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - To fix the logic of the hints, Claude suggested to swap the hint messages. (If the guess is too high, then the hint should be to go lower)
    - I verified by applying the changes and retrying the game with the changed code, and the hints are now correct as expected.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    - When prompting Claude to fix a bug of showing the wrong number of attempts when guesses are invalid, it pointed out another bug of numbers being compared lexicographically as strings rather than numerically, but when verifying the result, I didn't notice it to be a bug when playing the game. 
    - it also recommended adding a complicated line that looked unnecessary: "sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))"

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
