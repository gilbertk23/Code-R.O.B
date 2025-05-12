# Security Design Document

### Assets to Consider

- GUI Main
- Main executable program
- Objects (Getters / Setters / Construcotrs)

### Threats to Assets

#### Main / GUI Main Executable

- Malicious users
- Improper overwriting
- Pages being scraped
- Improper user input

#### Objects

- Incorrect use getters / setters / helpers
- Incorrect use of variables (not being private)
- Improper user input
- Malicious Users

### Security Measures

#### Main / GUI Main Executable

- Try and except all input to handle, format, and validate all data correctly
- Input validation black box functions
- User given very limited access to limit any accidental or malicious problems cause by the user
- Clean, check, and return the correct user input matching the variable needed <int> <float> etc...

#### Objects

- Try and except all input to handle, format, and validate all data correctly (if can be done)
- Input validation make sure setters and getters are correct
- Make sure the variables ARE PRIVATE

## Security Summary

Overall, the security we're dealing with mainly comes from the input validation and the clumsiness of the user itself and poorly written code.
We must make sure that we validate all functions and try to make sure we use try and catch statements. 
Our code must be safe with private variables and be clean.
Another thing that would be absolutely great just to add is the code being readable so that any person can gloss through it and see which function does what.

