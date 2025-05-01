employees.py
 
- Dictionary has key value pairs.

- Here "employees.py" is a dictionary where we have {key:{key:value}}

- So, this dictionary have keys and dectionaries as values.

- Here, key -> employees ID

- {key:value} -> employees Information
 
 
employees_data = {

  1:{

    "name": "Michael",

    "age": 42,

    "position": "Manager"

  },

  2:{

    "name" : "Jahir",

    "age" : 34,

    "position: "Senior"

  },

  3:{

    "name" : "Amit",

    "age" : 31,

    "position : "Senior"

  },

  4:{

    "name" : "Pam",

    "age" : 34,

    "position: "Manager"

  },

}
 
 
- now app.py
 
from employees import employees_data
 

 
 