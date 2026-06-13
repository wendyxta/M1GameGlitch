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
    - I used Claude Code, Sonnet 4.6 model on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - To fix the logic of the hints, where it gave backwards hints, Claude suggested to swap the hint messages. For example, if the guess is too high, then the hint should be to go lower, rather than go higher.
    - I verified by applying the changes and retrying the game with the changed code, and the hints are now correct as expected.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    - When prompting Claude to fix a bug of showing the wrong number of attempts when guesses are invalid, it pointed out another bug of numbers being compared lexicographically as strings rather than numerically, but when verifying the result, I didn't notice it to be a bug when playing the game. 
    - It also recommended adding a complicated line that looked unnecessary: "sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))". I don't think the game or logic has anything to do with files or paths so I didn't accep the suggestion and asked for alternate changes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - To decide if a bug was really fixed, I replayed the game, manaully performing the action that previously had a bug to see if the bug is still there, and seeing if the game now behaves as expected.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    - I used pytest to create test cases checking if it gave the correct hints. It showed me that when a guess was higher than the secret, my guess is too high, so the hint should say to go lower.
- Did AI help you design or understand any tests? How?
    - Yes, AI helped explain the logic in blocks of code and how the bugs can be fixed. It also helped be generate test cases that specifically test the bugs that were just fixed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    - A Streamlit rerun is when Streamlit executes the code again, refreshing the game. It gets triggered after ever button click or input change. Each rerun maintains session state, which keeps track of the game details and values of that session, until the game is restarted or the tab is closed.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? his could be a testing habit, a prompting strategy, or a way you used Git.
    - One strategy that I want to reuse in future projects is giving AI clear prompts and manually verifying the suggestions that AI provides. It is important to be specific in prompts, providing clear method names and specify specific blocks of code for AI to focus on by using markers like #FIXME to get better and more efficient responses.
- What is one thing you would do differently next time you work with AI on a coding task?
    - Next time I work with AI on coding tasks, I would like to create new conversation tabs more frequently so decrease the conversation history that AI scans through each time and decrease token usage. I definitely noticed the tokens increasing after each message and the responses taking longer to generate as I sent more messages in a conversation tab.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    - AI generated code provides a good basic framework of what you want to build, but it contains a lot of bugs that should be checked over and modified by humans. 
