# QA-Devops-Fundamental-Project - Library App
• This repo contains my work for the QA DevOps Fundamental Project <br>

## Contents
1. [Project Brief](#project-brief)
2. [Requirements](#requirements)
3. [App Design](#app-design)
4. [Version Control](#version-control)
5. [Risk Assessment](#risk-assessment)
6. [Testing](#testing)
7. [The Application](#the-application)


## Project Brief:
The brief for this project was as following:
    "Your overall objective with this project is the following:
    
    - To create a CRUD application with utilisation of supporting tools, methodologies and technologies 
      that encapsulate all core modules covered during training."

## Requirements
• A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.

• A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship.

• Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.

• A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board

• Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.

• A functioning front-end website and integrated API's, using Flask.

• Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

## App Design
### Trello Board
I used a Trello Board for project tracking using the MoSCoW prioritisation system. 
Below is the initial stage of the Project tracking
![1st Trello Board](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/kanban.PNG)
And below is after the MVP was achieved
![2nd Trello Board](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/kanban-finished.PNG)

### Entity Relational Diagram
This Library Application allows the user to create, read, update and delete books and authors. This is achieved through the Author and Book tables, which have a one-to-many relationship. The ERD is show below

![MVP ERD](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/edr.PNG)

## Version Control
I used Git for version control and hosted the project repo on Github. I used seperate branches whilst creating this project. I worked on a development branch named 'dev', and used seperate feature branches when adding new functionality (these branches were deleted on merges with dev branch) When I achieved the MVP, I merged the development branch with the main branch.

## Risk Assessment
A risk assessment was made to examine risks related to the project, including its requirements and its demands. Due to the detail of my risk assessment, I have opted to include it in my repo as a file, and it can be accessed [here](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/library-app-ra.xlsx).

## Testing
Currently, unit testing has been implemented. This tests functions in the application (it tests the create, read, update and delete functionalities). Coverage is currently at 97%.

![Coverage](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/coverage-report.PNG)

## The Application         
The user is first brought to the home page, which has a list of links.
![Home Page](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/home.PNG)

They can click a number of links. When they click on the "Add Book to our system" link, they will be taken to a page where they can input the title of a book.

![Add Book](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/add%20book.PNG)

They can then see the book in the database by clicking "View Books".

![View Books](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/view%20books.PNG)

They can add an Author to the database by clicking "Add Author to our table"

![Add Author](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/add%20author.PNG)

They can then view the authors that are in the table by clicking "View Authors".

![View Authors](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/view%20authors.PNG)

If they want to update an author, the user can update it manually by editing the url bar.

![Update Authors](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/update%20author.PNG)

And they can delete it manually by editing the url bar.
![Delete Author](https://github.com/Finneyyy/Devops-Fundamentals-Project-QA/blob/main/docs/delete%20author%20(part%201).PNG)


## Future Work
• Add more tables relating to Books, ie: "Categories".<br>
• Show authors beside the books they have written.<br>
• I want to add in proper linkage so it's easier to update/delete books and authors.<br>

## Known issues
• One can't see the authors beside the books they have written.
• The update functionality is mostly broken






