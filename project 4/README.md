# Project 4

Download the file describing [state-to-state migration flows](https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2015/state-to-state-migration/State_to_State_Migrations_Table_2015.xls) in the USA from the US Census Bureau (you can download it by hand). the goal of the project is to perform the network analysis of the flows.

Load the data from the file into a Pandas dataframe. Hint: pd.read_excel('State_to_State_Migrations_Table_2015.xls',header=0,index_col=0,skiprows=6,skip_footer=8,na_values='N/A3') does a good job, but there will be irrelevant rows and columns in the table. 
Select the rows and columns whose names are valid US state names. You can download a Pythonized list of state names (and symbols) [here](http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/). Restrict the list to 50 states and DC (no territories).
Replace missing values with 0.
Replace each value in the dataframe with true or False, depending on whether or not it is greater than the median flow. Remove the False rows. Unstack the resulting dataframe (you will get a multiindex), drop missing values, and convert the index of the resulting series into a list with .tolist(). You will get a list of 2601 or so significant flows.
Let each flow represent an edge of an undirected graph. Create an empty Graph and add the edges to it (the nodes will be added automatically.) Remove self loops.
Make your program answer the following questions:
Which 5 states have the highest betweenness centrality?
Which 5 states have the highest closeness centrality?
How many connected components does the network have?
How many communities are in the network, what states belong to each community, and what is the modularity of the community structure?
Extra credit: Save the resulting network into a GraphML file, load into Gephi, apply ForceAtlas2 layout, calculate modularity, color nodes by modularity class, display labels (state names), and save the file as a PDF image.