Jessica Schonhut-Stasik 
Assignment 1 

The following files in the directory can be run. 
homework_1.py
collatz_plot.py 

To run homework_1.py input to the command line: 

	python3 homework_1.py 

Output from homework_1.py is the file collatz_list_code_output.txt

To run collatz_plot.py input to the command line: 

        python3 collatz_plot.py

Output from collatz_plot.py are the plot files plot_range_1.png, plot_range_2.png, and plot_range_3.png.

The following files are data or plot files and cannot be executed in the command line:
assignment_1.pdf
collatz_sequence_hand.txt
week1.doc 
plot_range_1.png
plot_range_2.png
plot_range_3.png
collatz_list_code_output.txt

Answers to text questions from Assignment 1:
– To improve speed for this program we can use the fact that there is only one correct result for each individual number. For example, when N = 10, f(N) = 5. This will always be the case regardless of where the '10' falls within the list. Because we know the value 10 has a specific output, 5, we also know that 5 has a specific output. Therefore, by saving previous lists that have already been found, we can append these to future lists to speed up the creation process without having to pull the odd and even functions each time. 


