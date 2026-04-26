STRESS AND STRAIN CALCULATOR (PRELIM  PROJECT)

Introduction of the Program:
    - The program applies all that was learned (basics of python, functions, loops, OOP, etc.) and condense it into one
    file. The prompt asks to create a stress and strain calculator with the necessary functions (prompted input, calculations,
    control structures, output, code quality). In addition to other enhancement changes. In this program all said requirements
    and some enhancements were implemented.


To Run the Program:
    - To run the program you could either...
        - Run it through an IDE (PyCharm, Spyder, etc.)
        - Open command prompt and enter {python -m stress_strain.main} or {python stress_strain/main.py} to run this program
    - In my end I had to first open the folders through {cd "C:\Users\User\Python Projects\Yutuc_Thom_StressStrain"} then run
    {python -m pip install pandas} and {python -m pip install matplotlib} to be able to run {python -m stress_strain.main}
    - Note if you were to run it in both make sure the module versions are consistent (pandas and numpy)


Enhancements Selected:
    - Unit Conversion (Stress converted to psi in addition so did Young's Modulus)
    - Session Summary (Summary statistics of all inputs and outputs added)
    - File Logging (Each runs are exported as CSV. If a file already exists, append new outputs to that file)
    - Plot (Plot the stress {x} and strain {y} points in a scatterplot for all recorded sessions)
    - Note: Outputs in the program are in 4 decimal places but in the CSV the full value will be displayed
