#  Encoder/Decoder Project

This is a simple Python project that allows you to **encode** or **decode** words using basic string manipulation logic.

It was created as part of my Python learning journey.

---

##  Features

- Encode any word or sentence by adding a custom prefix and suffix
- Decode encoded words back to their original form
- Handles empty input and invalid choices
- Beginner-friendly Python logic using conditionals and loops

---

##  How It Works

- When encoding:
  - If the word length is ≥ 3:  
    - Move the first character to the end  
    - Add a fixed prefix (`dsf`) and suffix (`jkr`)
  - If the word length is < 3:  
    - The word is reversed directly
- When decoding:
  - If word ends with `jkr` and starts with `dsf`:  
    - Remove the prefix and suffix  
    - Move last character to front
  - If word length < 3:  
    - It’s reversed again

---

##  Run the Project

Make sure you have Python installed.

```bash
python encoder_decoder.py
