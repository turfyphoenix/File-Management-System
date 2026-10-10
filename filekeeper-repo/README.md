# Filekeeper

A small Python program that creates, reads, updates and deletes text files from a numbered terminal menu.

Live demo and code walkthrough: https://YOUR-USERNAME.github.io/YOUR-REPO/

## Run it

You need Python 3. There are no packages to install.

```
python file_manager.py
```

On some systems the command is `python3`. Files are created in the folder you start the program from, so try it in an empty folder first.

## Menu

```
===== FILE MANAGEMENT SYSTEM =====
1. Create a file
2. Read a file
3. Update a file
4. Delete a file
5. Exit
```

| Option | What it does |
| --- | --- |
| 1 Create | Asks for a file name. Refuses if the file already exists, otherwise asks for text and writes it. |
| 2 Read | Prints the contents of a file, or says it does not exist. |
| 3 Update | Rename the file, append a line, or overwrite the contents. |
| 4 Delete | Removes the file by name. There is no confirmation prompt. |
| 5 Exit | Ends the program. |

## Known quirks

These are things I noticed and may fix later.

- Overwrite (Update, option 3) writes a blank line before the new text, and its prompt says "appended".
- Any number other than 1, 2 or 3 at the Update menu returns to the main menu without a message.
- Typing letters instead of a number at the Update menu prints a Python error, which the program catches.
- `exitfile()` is defined but never used.

## Files

| File | Purpose |
| --- | --- |
| `file_manager.py` | The program |
| `index.html` | Project page with an in-browser demo (a simulation, not the real program) |

## Publish the page with GitHub Pages

Repository Settings, then Pages, then set the source to "Deploy from a branch", pick `main` and the `/ (root)` folder, and save. The page will appear at the address shown at the top of that settings screen.
