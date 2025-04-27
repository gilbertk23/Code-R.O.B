# Coding Standards and Practices Statement
The following standards and practices will be effect throughout the entire project's development:
- The Python programming language will be the only programming language used.
- All directories are named in titlecase. `ex: Example_Dir_Name`
- All variables and functions are written in lowercase snake case. `ex) example_var_name, example_function_name(param_1, param_2)`
- Constants are named in uppercase snake case. `ex) EXAMPLE_CONSTANT_NAME`
- Comments must be utilized for each major function.
  - single `#` for notes and descriptions.
  - triple `###` for named sections `ex) ### Section Name ###`
- All functions should have only one clearly-defined purpose, be no longer than ten lines long.
  - Note: Constructors and to-string functions are exempt from this clause.
  - Any other exceptions to this rule must have a clear rationale written in a comment.
- The program should follow proper OOP etiquette
  - private data attributes are only directly referenced within getters and setters
  - Superclass-subclass paradigm is followed if applicable
- Tiles on the game map will be 16x16 pixels
- Sprites (players, NPCs, items) on the game map will be 32x32 pixels
