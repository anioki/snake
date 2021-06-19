# Snake game
Training project classic snake game  
  
## Project description  
### Structure of project 

```` 
snake
    ├── env                  - contains files with environmental elements.
    │   ├── core             - main parts of env. 
    │   │   ├── snake.py     - snake properties.
    │   │   └── world.py     - grid world properties.
    │   │
    │   ├── utils            - additional parts of env
    │   │   └── renderer.py  - observation rendering tool. 
    │   │
    │   └── snake_env.py     - compilation of main parts of environment.
    │
    ├── settings             - here you can store different constant values, connection parameters, etc.
    │   └── constants.py     - multiple constants storage for their convenient usage.
    │
    └── interactor.py        - script to allow you playing Snake manually.

````   
### In work  
World size is 32x32 blocks. Rules of the game are the same as the classic snake game.  
The goal of the project was to create something easy and trivial for understanding and new for me from a programming point of view.  
Example of game:
![Example screen](https://user-images.githubusercontent.com/77074682/122652535-1b409580-d148-11eb-93d5-c310e032bd43.gif 'Example screen')  

