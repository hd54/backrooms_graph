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

We also need to set up Javascript environment, which can be downloaded here: https://nodejs.org/en#download. The IDE
will detect the environment automatically, but if not please restart Pycharm. After this, you will be able to use npm
commands. You will need to install Webpack and Babel as well as some libraries. The full details may be found here:
[Instruction Video](https://www.youtube.com/watch?v=6c2NqDyxppU&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j&index=3&t=2s)

In short, you will need to run these following commands (note that --legacy-peer-deps is needed for some commands since
they don't work well with React 18):
* npm i webpack webpack-cli --save-dev
* npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
* npm i react react-dom --save-dev 
* npm install @material-ui/core --legacy-peer-deps
* npm install @babel/plugin-proposal-class-properties --legacy-peer-deps
* npm install @material-ui/icons --legacy-peer-deps

To run the program, the directory should be set to backrooms_site/frontend. After that, run npm run dev. If all goes well,
go back to folder backrooms_site and run python manage.py runserver to launch the local server.

## Phase 3: Front-end development

WIP

### Credits:
* Data from http://backrooms-wiki.wikidot.com/
* Django and React setup from [TechWithTim](https://www.youtube.com/@TechWithTim)
