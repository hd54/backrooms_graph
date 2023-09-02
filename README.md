# Backrooms Graph

The Backrooms are a fictional, alternate dimension outside the scope of the reality.
Thus, a person ending up at the Backrooms is the result of "no-clipping", glitching through solid environments.

This project aims to provide users an interactive guide in navigating through different levels of the backrooms.
The project stores a SQLite3 database of all existing levels' information and display the levels as nodes of the
graph. Users may click on the node for more information.

The project has been divided into several phases:

## Phase 1: Create database

We use beautifulsoup4 to help with scraping the data from the website: http://backrooms-wiki.wikidot.com/. We will store
these data in a SQLite3 database. This whole process can be found in db_extract.py. We have also connected the database
to Django and define the models.

A graph visualization using networkx and pyplot is given in graph.py after running the file, despite being not very effective due to
the amount of nodes we have in the graph.

## Phase 2: Set up environments

We use the version 3.11.4 Python. The environment is set up by Anaconda, which can be found in https://www.anaconda.com/download.
Pycharm IDE is used for the project. Most packages will be automatically installed when Anaconda is set up but here are
the important ones that are needed for the project to work:
* Django
* beautifulsoup4 
* djangorestframework
* regex
* requests
* urllib3

I also need to set up Javascript environment, which can be downloaded here: https://nodejs.org/en#download. The IDE
will detect the environment automatically, but if not please restart Pycharm. After this, users will be able to use npm
commands. Users will need to install Webpack and Babel as well as some libraries. The full details may be found here:
[Instruction Video](https://www.youtube.com/watch?v=6c2NqDyxppU&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j&index=3&t=2s)

In short, users will need to run these following commands. If some commands are not executed successfully, please add --force
or --legacy--peer-deps to the original command:
* `npm install webpack webpack-cli --save-dev`
* `npm install @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`
* `npm install react react-dom --save-dev`
* `npm install @babel/plugin-transform-class-properties --legacy-peer-deps`
* `npm install cytoscape --legacy-peer-deps` (phase 3)
* `npm install cytoscape-cose-bilkent --legacy-peer-deps` (phase 3)

To run the program, the directory should be set to backrooms_site/frontend. After that, run npm run dev. If all goes well,
go back to folder backrooms_site and run python manage.py runserver to launch the local server.

I have set up the API from the database, which can be accessed at http://127.0.0.1:8000/backrooms/api after users successfully
run the local server.

## Phase 3: Front-end development

I used [Cytoscape](https://cytoscape.org/), an open source platform dedicated to network visualization. I fetched API to create
nodes and edges that carry information of each level. I also adjusted the graph to be fully displayed on screen and styling for a
more appealing graph.

## Accomplishments

* How to develop a full stack application using multiple frameworks
* Picked up Python and Javascript

## Improvements

There is always room for improvements. I would love these features to be implemented and adjusted, such as:
* Producing the complete database: I managed to scrap most of the data besides a few levels with much different HTML
structures compared to the rest and would thus want to work with these unique levels.
* Adding new features to the server, such as allowing users to expand and collapse the graph, or to be directed to the
official wiki through on-click events.

### Credits:
* Data from http://backrooms-wiki.wikidot.com/
* Django and React setup from [TechWithTim](https://www.youtube.com/@TechWithTim)
