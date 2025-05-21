The random walk simulation website is a way to show a random walk through 1000 steps on your web browser. 

***Procedure***

The simulation works by getting a random number between -1 and 1 and then normalizing the value to correspond to each step being approximately the same size. The number is then added to a pre-determined origin value and then stored in 2 arrays for x and y values. The process repeats itself for 1000 steps until the array is fully populated.

The graph is created through Dash and Plotly. In order to run the graph, simply do the command

python random_walk.py

and a Dash server will be created from which you can access the website at http://127.1.1.1:8050/.

One can also decide to redo the simulation when they want to through the "Generate values" button at the top-left of the screen. One also has the option to zoom in and out and pan through the graph through the controls on the upper-right of the screen.