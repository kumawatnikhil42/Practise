# Linux :

# cd /path/to/directory                             # to move on particular dir
# ls                                                # to files or folder in directory
# mkdir foldername                                  # to create a folder
# touch filename.extentension                       # to create a file
# pwd                                               # to know current working directory
# rmdir foldername                                  # to delete folder
# rm filename.txt                                   # to delete file
# rm -r foldername                                  # delete folder with its content
# cp (copy)filename/foldername (paste)path/to/dir   # to copy file or folder 
# mv (move)filename/foldername (paste)path/to/dir   # to move file or folder 


# SQL:

# create table Departments (
#     department_id int PRIMARY KEY,
#     department_name VARCHAR(50) NOT NULL
# );

# CREATE TABLE Employees (
#     employee_id INT PRIMARY KEY,             -- Primary Key Constraint
#     first_name VARCHAR(50) NOT NULL,         -- Not Null Constraint
#     last_name VARCHAR(50),
#     department_id INT,
#     salary DECIMAL(10, 2) CHECK (salary > 0), -- Check Constraint
#     hire_date DATE DEFAULT CURRENT_DATE,     -- Default Constraint
#     email VARCHAR(100) UNIQUE,               -- Unique Constraint
#     manager_id INT,
#     FOREIGN KEY (department_id) REFERENCES Departments(department_id), -- Foreign Key Constraint
#     FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)         -- Self-referencing Foreign Key
# );

# select * from tablename;
# select * from tablename where condition;
# select first_name, last_name
# from Employees
# where department = 'Sales' or department = 'Marketing';



# Python:

# variables = these are containers for storing data values. In python you need not declare data type of a variable because python is a dynamic typed language which means interpreter determines its data type at runtime.

# Data types = it is a classification that specifies the kind of data that a variable or object can hold in programming.

# there are mainly 6 types:
# 
# 1. Numeric =>
# Integer(int) whole number
# Float(float) real number(decimal,negative,positive)
# complex(complex) complex numbers(a+ib)
#
# 2. String =>
# Sequence of characters defined by single,double or triple quotes.
#
# 3. Boolean =>
# Two values True and False
#
# 4. Sequence =>
# list => mutable and hold diffrent data types.
# tuple => immutable and cannot changed after creation.
#
# 5. Mapping=>
# Dictionary(dict)=> mutable and it stores key-value pairs. Each key is unique within a dictionary.
# 
# 6. Set =>
# Set(set) => mutable and collection of unique items.
# frozenset(frozenset) => immutable version of a set.


# Machine Learning:
# ML introduction => ml is a type of artificial intelligence that allows computers to learn without being explicitly programmed.
# It involves feeding data into algorithms that can be identify patterns and make predictions on new data.
#
# Types of Machine Learning =>
# 1. Supervised learning => it is the ml task and in this sample labeled data are provided to the machine learning system for training, and then predicts the output based on the training data.
# 
# 2. Unsupervised learning =>  it is used with data that has no labels. The model tries to find patterns and relationships in the data on its own.
# 
# 3. Reinforcement Learning => in reinforcement learning, an agent learns by interacting with an environment and recieving feedback through rewards or penalties.  


# Docker:
# 
# Docker is a platform for developing, shipping, and running applications in containers.
# Containers are lightweight and portable that can run applications and their dependencies in isolated envirronments.
#
# Docker Engine => the core of docker is the docker engine, which is responsible for building, running and managing containers.
# Docker Images => images are lightweight, standalone, and executable packages taht include everything needed to run a piece of software, including the code, libraries and system tools. Images are used to create container.
# Docker Container => containers are instances of docker images that run in isolated enviroments.
# 
# Docker Commands:
# 1. Build =>
# docker bulid -t image_name:tag    # build a docker image from a dockerfile in the current directory
# 
# 2. Docker Run =>
# docker run image_name:tag
#
# 3. Docker Push =>
# docker push image_name:tag
#
# Docker Setup =>
#   app.py
#   dockerfile      => FROM python:3.8
#                      COPY . /app
#                      WORKDIR /app
#                      RUN pip install -r requirements.txt
#                      CMD ["python3", "app.py"]
#   requirement.txt





