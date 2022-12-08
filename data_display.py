# Include neccessary Libraries
import json
import glob
from bokeh.io import show
from bokeh.models import TabPanel, Tabs
from bokeh.plotting import figure, show, output_notebook
  
# Initialize Variables and lists
file_names = []
loaded_data = []
countries = []
total_deaths = []
new_deaths = []
deaths_per_1m = []
new_deaths_per_1m = []
country_count_list = []
country_count = 1
old_country = ""
loop_count = 0
legend_list = []
y = []
x = []
days = []
t_deaths = []
n_deaths = []
deaths_per_mill = []
new_deaths_per_mill = []
index = 0
color = ["blue",
         "red",
         "green",
         "purple",
         "black",
         "orange",
         "bisque",
         "greenyellow",
         "magenta"]

# Read in all the file names from the folder
for names in glob.glob('json_files/*'):

    # open the json files
    with open(names) as json_file:
    
        # create loaded data varaible
        data = (json.load(json_file))
        key_values = list(data['Country,Other'].keys())
        countries.append(data['Country,Other'][key_values[0]])
        total_deaths.append(int(data['TotalDeaths'][key_values[0]].replace(',',"")))
        
        # New Deaths: Check to see if can convert to integer
        if data['NewDeaths'][key_values[0]] == "":
            
            # Convert string to zero
            new_deaths.append(0)
        
        # if has a , or + replace and convert to int  
        else:
            
            # Check for ,
            if ',' in data['NewDeaths'][key_values[0]]:
                
                # if , pressent remove
                new_deaths.append(int(data['NewDeaths'][key_values[0]].replace(',',"")))
                
            # Check for +
            if '+' in data['NewDeaths'][key_values[0]]:
                
                # if + pressent replace
                new_deaths.append(int(data['NewDeaths'][key_values[0]].replace('+',"")))
                
            else:
                
                # Convert to int
                new_deaths.append(int(data['NewDeaths'][key_values[0]]))
                
        # deaths_per_1m: Check to see if can convert to integer
        if data['Deaths/1M pop'][key_values[0]] == "":
            
            # Convert string to zero
            deaths_per_1m.append(0)
        
        # if has a , or + replace and convert to int  
        else:
            
            # Check for ,
            if ',' in data['Deaths/1M pop'][key_values[0]]:
                
                # if , pressent remove
                data['Deaths/1M pop'][key_values[0]] = data['Deaths/1M pop'][key_values[0]].replace(',',"")
                
            deaths_per_1m.append(int(data['Deaths/1M pop'][key_values[0]]))

        # New deaths_per_1m: Check to see if can convert to integer
        if data['New Deaths/1M pop'][key_values[0]] == "":
            
            # Convert string to zero
            new_deaths_per_1m.append(0)
        
        # if has a , or + replace and convert to int  
        else:
            
            # Check for ,
            if ',' in data['New Deaths/1M pop'][key_values[0]]:
                
                # if , pressent remove
                data['New Deaths/1M pop'][key_values[0]] = data['New Deaths/1M pop'][key_values[0]].replace(',',"")
                
            new_deaths_per_1m.append(float(data['New Deaths/1M pop'][key_values[0]])) 

    loop_count +=1

# Count the number of json files for each country
for i in range(loop_count-1):
    
    # Check the next element in a list
    if countries[i] == countries[i+1]:
        
        # Increment country file count
        country_count += 1
        
        # If at the end of the list count the last element
        if loop_count-1 == i+1:
        
            country_count_list.append(country_count)
        
    else:
        
        # Create list of count values of each country
        country_count_list.append(country_count)
        country_count = 1
    

# Create list of all the countries that were loaded in/ Remove duplicates
for j in countries:
    
    if j not in legend_list:
        
        legend_list.append(j)

# instantiating the figure object for total covid deaths
graph_total = figure(title="Total Covid Deaths")
graph_total.xaxis.axis_label = "Days"
graph_total.yaxis.axis_label = "Total Deaths"
 
# Loop through and create lists to graph covid data
for k in range(len(country_count_list)):
    
    # Create x data array of days and y data of deaths
    for l in range(country_count_list[k]):
        
        # create lists
        x.append(l+1)
        y.append(total_deaths[index])
        index += 1
    
    days.append(x)
    t_deaths.append(y)
    
    # plotting the 1st line graph
    graph_total.line(days[k], t_deaths[k], line_color=color[k], legend_label=legend_list[k], color=color[k])
    
    x = []
    y = []

index = 0

# instantiating the figure object for new covid deaths
graph_new_death = figure(title="New Covid Deaths")
graph_new_death.xaxis.axis_label = "Days"
graph_new_death.yaxis.axis_label = "New Deaths"
 
for k in range(len(country_count_list)):
    
    for l in range(country_count_list[k]):

        y.append(new_deaths[index])
        index += 1
    
    n_deaths.append(y)
    
    # plotting the line graph
    graph_new_death.line(days[k], n_deaths[k], line_color=color[k], legend_label=legend_list[k], color=color[k])
    
    x = []
    y = []
    
index = 0

# instantiating the figure object
graph_deaths_per_1m = figure(title="Total Deaths per 1 Million")
graph_deaths_per_1m.xaxis.axis_label = "Days"
graph_deaths_per_1m.yaxis.axis_label = "Deaths per 1M"
 
for k in range(len(country_count_list)):
    
    for l in range(country_count_list[k]):

        y.append(deaths_per_1m[index])
        index += 1
    
    deaths_per_mill.append(y)
    
    # plotting the 1st line graph
    graph_deaths_per_1m.line(days[k], deaths_per_mill[k], line_color=color[k], legend_label=legend_list[k], color=color[k])
    
    x = []
    y = []

index = 0

# instantiating the figure object
graph_new_deaths_per_1m = figure(title="New Deaths per 1 Million")
graph_new_deaths_per_1m.xaxis.axis_label = "Days"
graph_new_deaths_per_1m.yaxis.axis_label = "New Deaths per 1M"
 
for k in range(len(country_count_list)):
    
    for l in range(country_count_list[k]):

        y.append(new_deaths_per_1m[index])
        index += 1
    
    new_deaths_per_mill.append(y)
    
    # plotting the 1st line graph
    graph_new_deaths_per_1m.line(days[k], new_deaths_per_mill[k], line_color=color[k], legend_label=legend_list[k], color=color[k])
    
    x = []
    y = []


tab1 = TabPanel(child=graph_total, title="Total Covid Deaths")
tab2 = TabPanel(child=graph_new_death, title="New Covid Deaths")
tab3 = TabPanel(child=graph_deaths_per_1m, title="Total Deaths Per 1M")
tab4 = TabPanel(child=graph_new_deaths_per_1m, title="New Covid Deaths per 1M")
 
all_tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])
 
# Display all graphs and tabs
show(all_tabs)

    

