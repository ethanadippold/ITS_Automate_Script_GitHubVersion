# ITS-AutomateScript

A small Python script that automates the repetitive, uniform parts of call documentation for an IT Services (ITS) helpdesk. It walks through the standard identity-verification flow for a support call and prints out a documentation entry in the format the department requires, instead of typing the same boilerplate by hand every time.

## Why

At my ITS job, documentation has to follow a specific standard for every call, and most of the structure is the same regardless of the outcome. This script handles the "same every time" part automatically based on a few Y/N answers, so the only thing left to do is confirm what actually happened on the call.

## What it does

1. Asks for the attempt number (1st, 2nd, or 3rd) and labels the entry accordingly.
2. Asks whether ID verification was needed for the call.
3. If yes, walks through the verification steps (V-Step #1 through #3) and asks whether each one succeeded.
   - V-Step #4 is a failsafe: it only comes up if V-Step #2 or V-Step #3 fails, as the alternate verification method for that case.
4. Prints a formatted documentation entry showing which steps passed, headed by the attempt label.

## A note on "V-Step"

The actual verification methods are internal ITS procedure, so the specific step names have been replaced here with generic V-Step #1–#4 labels. The branching logic is unchanged; only the labels are genericized for public visibility.

## Usage

```bash
python3 ITS-AutomateScript.py
```

You'll be walked through a series of Y/N prompts. At the end, the script prints a documentation entry ready to copy into a ticket or call log.

### Example

```
Enter attempt number: 1
ID Verification Needed? (Y/N) Y
V-Step #1? (Y/N) Y
V-Step #2? (Y/N) Y
V-Step #3? (Y/N) Y
First attempt
Information Verified
V-Step #1: Y
V-Step #2: Y
V-Step #3: Y
```

## Requirements

- Python 3

## Status

Actively in progress. This version documents a single call per run; a version with a restart loop and a dedicated call-handling function is in development.
