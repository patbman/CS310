# Project 3

File trades.txt (attached) contains real Forex trading data related to an anonymous trader. The file has tabular structure and has 4 columns:

openTime - open trade time in milliseconds;
openPrice - opening share price in dollars; 
closePrice - closing share price in dollars;
volume - number of traded shares.
Write a program that shall use NumPy and Pyplot to read and analyze the data in the file. The program shall automatically produce the following outputs:

A scatter plot that shows the cumulative account balance as a function of time.
At each trade, the balance changes by (closePrice-openPrice)*volume.
The X axis of the plot shall be labeled in days, assuming that the first trade took place at midnight of day 0.
Both axes shall be properly labeled.
The plot shall have a proper title and a colorbar.
The color of a point shall represent the balance change associated with the point.
The points shall be connected with a line. (Consider combining plot() and scatter().)
The plot shall have both vertical and horizontal grid lines.
A histogram showing the distribution of gains/losses for all trades.
The histogram shall have no fewer than 25 bins.
Both axes of of the histogram shall be properly labeled. 
The histogram shall have a proper title.
A pie chart that shows the fraction of trades with positive, negative, and zero values (three wedges).
The wedges of the pie shall be properly labeled.
The chart shall have a proper title.
The program shall save the outputs as PNG files with the resolution of 200dpi. The program shall not display the images. The program shall not use any loops or list comprehensions. 