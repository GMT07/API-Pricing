My Web API
==========


# Pricing of derivative and exotic options

My app is a Python API to manage the pricing of derivative and exotic options.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all packages.

## Setup

- Install Python 3 and git.
- Run `config.bat` (Windows)
- Run `./my_app.py` to start the server (on Windows)
- Open `http://localhost:5000/` on your web browser to login the user

## Testing on [Postman](https://www.postman.com/downloads/)

### 1. Get description about a specific parameter 
```python
$ GET /guy/api/v1.0/tasks

Response
Status: 200 OK
Location: http://localhost:5000/guy/api/v1.0/tasks
{
  "tasks": [
    {
      "description": "Pricing of derivative options with Monte Carlo method",
      "done": false,
      "title": "Derivative option",
      "uri": "http://localhost:5000/guy/api/v1.0/tasks/1"
    },
    {
      "description": "Pricing of exotic options with Monte Carlo method",
      "done": false,
      "title": "Exotic option",
      "uri": "http://localhost:5000/guy/api/v1.0/tasks/2"
    }
  ]
}
```

### 2. Get description about a specific product by specifying its id

```python
$ GET /guy/api/v1.0/tasks/:task_id

Response
Status: 200 OK
Location: http://localhost:5000/guy/api/v1.0/tasks/:task_id
{
  "task": {
    "description": "Pricing of exotic options with Monte Carlo method",
    "done": false,
    "title": "Exotic option",
    "uri": "http://localhost:5000/guy/api/v1.0/tasks/2"
  }
}
```

### 3. POST an option price and description about a specific parameter

```python
$ POST /guy/api/v1.0/tasks

Example: Format Json
{
    "title": "Pricing option",
    "description": "Vanilla option", 
    "option_type": "Vanilla_Put", 
    "spot": 100.0, 
    "strike": 100.0, 
    "risk_free": 0.01, 
    "volatility": 0.1, 
    "maturity": 1.0
}

Response
Status: 201 CREATED
Location: http://localhost:5000/guy/api/v1.0/tasks
{
  "task": {
    "delta": -0.40900642467712744,
    "description": "Vanilla option",
    "done": true,
    "maturity": 1.0,
    "option_type": "Vanilla_Put",
    "price": 3.44081211209072,
    "risk_free": 0.01,
    "volatility": 0.1,
    "spot": 100.0,
    "status": "Returns a price and delta of vanilla option",
    "strike": 100.0,
    "title": "Pricing option",
    "uri": "http://localhost:5000/guy/api/v1.0/tasks/3"
  }
}
_
```

## Range of parameter values

### I. Pricing of path independent options
### 1. Vanilla options
```json
{
    "title": ,
    "description": ,
    "option_type": , 
    "strike": , 
    "maturity": ,
    "spot": ,
    "volatility": ,
    "risk_free": 
}
```
```text 
NB: - description in {"Vanilla option", "Double digital option", "Asian option", "Lookback option", "Basket option", "Best of option", "Worst of option"}
    - option_type in {"Vanilla_Call", "Vanilla_Put", "Cash_Or_Nothing_Call", "Cash_Or_Nothing_Put", "Asset_Or_Nothing_Call", "Asset_Or_Nothing_Put"}
```

### 2. Pricing of doubles digital options
```json
{
    "title": ,
    "description": ,
    "option_type": ,
    "low": ,
    "up": ,
    "strike": ,
    "maturity": ,
    "spot": ,
    "volatility": ,
    "risk_free":  
}
```
```text
NB: - description in {"Double digital option"}
    - option_type in {"Double_Digital"}
```

### II. Pricing of path dependent options
### 3. Pricing of asian options
```json
{
    "title": ,
    "description": ,
    "option_type": ,   
    "strike": , 
    "maturity": ,
    "spot": ,
    "volatility": ,
    "risk_free": 
} 
```
```text
NB: - description in {"Asian option"}
    - option_type in {"Arithmetic_Average_Call", "Arithmetic_Average_Put", "Geometric_Average_Call", "Geometric_Average_Put", "Arithmetic_Floating_Call", "Arithmetic_Floating_Put", "Geometric_Floating_Call", "Geometric_Floating_Put"}
```

### 4. Pricing of look-back options
```json
{
    "title": ,
    "description": ,
    "option_type": , 
    "strike": ,
    "maturity": ,
    "spot": ,
    "volatility": ,
    "risk_free":  
}
```
```text
NB: - description in {"LookBack option"}
    - option_type in {"lookBack_Call", "lookBack_Put"}
```

### 5. Pricing of Basket options
```json
{
    "title": ,
    "description": ,
    "option_type": , 
    "a": ,
    "b": ,
    "strike": ,
    "maturity": ,
    "spot1": ,
    "spot2": ,
    "vol1": ,
    "vol2": ,
    "rho": ,
    "risk_free":  
}
```
```text
NB: - description in {"Basket option"}
    - option_type in {"Basket_Call", "Basket_Put"}
```

### 6. Pricing of Best of and Worst of options
```json
{
    "title": ,
    "description": ,
    "option_type": , 
    "strike": ,
    "maturity": ,
    "spot1": ,
    "spot2": ,
    "vol1": ,
    "vol2": ,
    "rho": ,
    "risk_free":  
}
```
```text
NB: - description in {"Best of option", "Worst of option"}
    - option_type in {"BestOf_Call", "BestOf_Put", "WorstOf_Call", "WorstOf_Put"}
```

## Contributing
Pull requests are welcome. 

Tools
-----

- GET : http://localhost:5000/guy/api/v1.0/tasks 
- GET : http://localhost:5000/guy/api/v1.0/tasks/task_id
- POST : http://localhost:5000/guy/api/v1.0/tasks
- PUT : http://localhost:5000/guy/api/v1.0/tasks/task_id
- DELETE : http://localhost:5000/guy/api/v1.0/tasks/task_id
