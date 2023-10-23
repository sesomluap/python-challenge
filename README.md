I started both parts of the challenge the same way: by importing the os and csv libraries, creating a joined path, and opening the csv file I was working with. 
This was covered in a number of in class examples but I will admit I needed help from all of askBCS, tutoring, and office hours to really nail down my  paths
On both parts the next step was the same, I needed to skip the header and analyze the rest

First, PyBank: I needed to create a lists containing each of the months and profit numbers contained in the csv
I calculated total months by finding the length of the list I had created
I then used the profit list to create a new list with all of the monthly changes in profit
I used the monthly change list to calculate the rounded average of monthly changes
Next I used max and min functions to find the greatest month to month increase and decrease
Finding the corresponding month was trickier than finding the change itself, but with some help from Stack Overflow and debugging with ChatGPT I got there
All that was left was printing and outputting the results!

PyPoll required a little more setup, I needed 3 initial lists and a vote counter variable starting at 0
The first thing I wanted my loop to do was count every vote for the total
Next I had to identify each of the unique candidates, while still making sure I counted the vote where their name first appeared
The rest of the loop tallied the vote. While the results were ordered on the csv, I think this loop would also work if the candidate names had been scattered randomly
I then portioned out each candidates' vote totals as rounded percentages
I used the max function to find the winner
Outputting the results here was a little trickier--I used a loop to pull the correct vote counts and % for each candidate
I played around with using variables to duplicate my work across the print and write functions, but the loop didn't transfer correctly so I kept everything as manual entries
Made sure I put both .txt files into their respective analysis folders, then pushed the changes here to finish!

Initially, my main sources were in-class examples, W3 Schools, Real Python, and Stack Overflow
As I ran into trouble I sought help from my study groups, office hours (for path problems), ChatGPT, and askBCS
