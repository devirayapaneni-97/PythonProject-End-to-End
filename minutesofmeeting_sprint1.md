- What is the project about
 	---- The project involves developing a two-tier application, which essentially means separating the application into two parts: the client-side (front end) and the server-side (back end). 


- What is the tech stack
	----  In this project, I utilized Python as the programming language for both the client and server sides. For the database management system, I opted for MySQL.To build the server-side logic and APIs, I used Flask, a lightweight and flexible web framework for Python. 


- What is the architecture 
	---- The architecture of the project revolves around the client-server model, where the client (front end) communicates with the server (back end) to request and receive data. The Flask framework acts as the server, handling HTTP requests from the client and interacting with the MySQL database to retrieve or store data. The client-side could be implemented using various technologies such as HTML, CSS, and JavaScript to create a user-friendly interface that interacts with the Flask server via HTTP requests.


- What tools you used 
	--- Throughout the development process, I utilized GitHub to manage my project's source code, version control, and collaboration with other team members. Additionally, I used  DBeaver as a database management tool to connect to the MySQL database, execute queries, and inspect table structures and data.


- What challenges you faced.
	---One of the challenges I encountered during the project was initially setting up the connection between the Flask application and the MySQL database. This required troubleshooting and ensuring that the database configuration was correctly specified in the Flask application. Additionally, I faced issues related to file paths while running the app.py file locally, which was resolved by double-checking and correcting the path configurations in the code.

  
---application flow:
1. The flask application reads the data which is present in the messages table, retrive the data and display in UI
2. In UI if we enter any data, it gets stored in DATABASE where the table is messages.
