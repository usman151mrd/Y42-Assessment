# how to run
```shell
cd project_directory
python3 -m venv venv
source venv/bin/activate
pip install coverage
coverage run -m unittest # to run all test cases
coverage report # to watch code coverage
```

# Question 1 Explanation
 * create two custom exception classes as task required
 * create a class to implement stack data structure and also create required methods
 * implement logic in methods as task one required and write all test cases with 100% code coverage


# Question 2 Explanation
 * create an abstract class inspired by Django ORM
 * suppose to handle structured data so create product model with some attributes
 * Model class has a id which always unique so, it helpful  for update and delete operations
 * Model class has an abstract function to_dict that return object in dict format because here __dict__ not work because of all attribute declared in private mode and only accessible using properties
 * object dictionary easily parser in any other format like json and xml
 * declare a class Storage, and it can be extendable  by any other class
 * storage has 2 attribute filename and type, data has two types(binary, text)
 * so, filename can store filename with location address depends on the type of storage
 * 2 classes extends from Storage and, it depends on developer that how many type of storage they required to extend
 * an abstract class Data created that defined abstract methods mentioned in document
 * number of classes can b extendable for data with their formats, I handle json data abd create mock class with methods of cloud data
 * data can be written or read on storage with name load and dump inspired by pickle library
 * each and every class extendable like Django framework and no need to modify current classes
 * test cases are also written in test cases and provide method to run them at the top of file 
# what should improve in my code 
* split code into different files as each file has a single class
* add comment for each line
* create a python package that can be installed using pip, although I can do it easily and company provide me 72 hours but not possible for me to work all the time due to personal commitments

# Code best features
* all the code is implementing fully followed object-oriented OOP concept and also tried to follow SOLID principle as well
