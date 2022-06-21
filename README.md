# psychopyRaCo
Automatic conditions file selection with self-balancing random procedure for PsychoPy. Randomly selects a conditions file with weighted random procedure. For each file the weight is inversely proportional to the number of uses. Weighted random doesn't work for Pavlovia yet. 

## Installation:
### For balanced random (local):
1. Place the `problems_randomisation.csv` file in the `assets` subfolder of your PsyhoPy project
2. Edit the `problems_randomisation.csv` file so it has the names of your condition files
3. Make sure that there's a `,1` in each line after a conditions file name
4. Open your PsychoPy project in PsychoPy
5. Add the "Code" component in the first routine and open it
6. Paste the code from `begin_experiment.py` file into the `Begin experiment` tab
7. Click `Ok` and save the project
8. I would be happy if you cite this repository in your paper

### For plain random (local):
1. Download the `begin_experiment.py` file and open it in any text editor
2. Find the line that says `fileIndex = random.randint(1, 4)` (closer to the end of the file, line 93 initially)
3. Change the second number to a number of conditions files that you have
4. Open your PsychoPy project in PsychoPy
5. Add the "Code" component in the first routine and open it
6. Paste the code from `begin_experiment.py` file into the `Begin experiment` tab
7. Click `Ok` and save the project
8. Make sure all your conditions file are named `conditions#` where `#` is a number. Numbers should start from 1 and go sequentional (1, 2, 3 ...)
9. I would be happy if you cite this repository in your paper

### For plain random (Pavlovia):
1. Download the `begin_experiment.js` file and open it in any text editor
2. Find the line that says `var fileIndex = getRandomIntInclusive(1, 4)`
3. Change the second number to a number of conditions files that you have
4. Open your PsychoPy project in PsychoPy
5. Add the "Code" component in the first routine, open it and set "Only JS"
6. Paste the code from `begin_experiment.py` file into the `Begin experiment` tab
7. Click `Ok` and save the project
8. Make sure all your conditions file are named `conditions#` where `#` is a number. Numbers should start from 1 and go sequentional (1, 2, 3 ...)
9. I would be happy if you cite this repository in your paper
