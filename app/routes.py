#!/usr/bin/env python
import six
from pricingFI import pricer
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from config import *

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),
                                                 password):
        return username


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.current_user()


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


tasks = [
    {
        'id': 1,
        'title': u'Derivative option',
        'description': u'Pricing of derivative options with Monte Carlo method',
        'done': False
    },
    {
        'id': 2,
        'title': u'Exotic option',
        'description': u'Pricing of exotic options with Monte Carlo method',
        'done': False
    }
]


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'],
                                      _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/guy/api/v1.0/tasks', methods=['GET'])
@auth.login_required
# @auth.verify_password
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/guy/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': make_public_task(task[0])})


@app.route('/guy/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or 'description' not in request.json:
        abort(400)

    if request.json['description'] == "Vanilla option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],
            'option_type': request.json['option_type'],
            'spot': request.json['spot'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'volatility': request.json['volatility'],
            'maturity': request.json['maturity'],
            'done': False
        }

        option_type = task['option_type']
        spot = task['spot']
        strike = task['strike']
        interest_rate = task['risk_free']
        volatility = task['volatility']
        maturity = task['maturity']

        price = pricer.MonteCarloOneUnderlying(option_type, strike, maturity, spot, volatility, interest_rate, 10000.0)
        delta = pricer.DeltaOptionVanilla(option_type, strike, maturity, spot, volatility, interest_rate, 10000.0)
        task['price'] = price
        task['delta'] = delta
        task['done'] = True
        task['status'] = "Returns a price and delta of vanilla option"
    elif request.json['description'] == "Double digital option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],  # request.json.get('description', ""),
            'option_type': request.json['option_type'],
            'spot': request.json['spot'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'volatility': request.json['volatility'],
            'maturity': request.json['maturity'],
            'low': request.json['low'],
            'up': request.json['up'],
            'done': False
        }

        option_type = task['option_type']
        spot = task['spot']
        interest_rate = task['risk_free']
        volatility = task['volatility']
        maturity = task['maturity']
        low = task['low']
        up = task['up']

        price = pricer.MonteCarloDoubleDigital(option_type, low, up, maturity, spot, volatility, interest_rate, 10000.0)
        delta = pricer.DeltaOptionDoubleDigital(option_type, low, up, maturity, spot, volatility, interest_rate, 10000.0)
        task['price'] = price
        task['delta'] = delta
        task['done'] = True
        task['status'] = "Returns a price and delta of double digital option"
    elif request.json['description'] == "Asian option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],  # request.json.get('description', ""),
            'option_type': request.json['option_type'],
            'spot': request.json['spot'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'volatility': request.json['volatility'],
            'maturity': request.json['maturity'],
            'done': False
        }

        option_type = task['option_type']
        spot = task['spot']
        strike = task['strike']
        interest_rate = task['risk_free']
        volatility = task['volatility']
        maturity = task['maturity']

        price = pricer.MonteCarloAsianOptions(option_type, strike, maturity, spot, volatility, interest_rate,
                                              100.0, 10000.0)
        delta = pricer.DeltaAsianOptions(option_type, strike, maturity, spot, volatility, interest_rate,
                                         100.0, 10000.0)
        task['price'] = price
        task['delta'] = delta
        task['done'] = True
        task['status'] = "Returns a price and delta of asian option"
    elif request.json['description'] == "LookBack option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],  # request.json.get('description', ""),
            'option_type': request.json['option_type'],
            'spot': request.json['spot'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'volatility': request.json['volatility'],
            'maturity': request.json['maturity'],
            'done': False
        }

        option_type = task['option_type']
        spot = task['spot']
        strike = task['strike']
        interest_rate = task['risk_free']
        volatility = task['volatility']
        maturity = task['maturity']

        price = pricer.MonteCarlo_LookBack(option_type, strike, maturity, spot, volatility, interest_rate, 100.0,
                                           10000.0)
        delta = pricer.Delta_LookBack(option_type, strike, maturity, spot, volatility, interest_rate, 100.0, 10000.0)
        task['price'] = price
        task['delta'] = delta
        task['done'] = True
        task['status'] = "Returns a price and delta of look-back option"
    elif request.json['description'] == "Basket option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],  # request.json.get('description', ""),
            'option_type': request.json['option_type'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'maturity': request.json['maturity'],
            'a': request.json.get('a', ""),
            'b': request.json.get('b', ""),
            'spot1': request.json.get('spot1', ""),
            'spot2': request.json.get('spot2', ""),
            'vol1': request.json.get('vol1', ""),
            'vol2': request.json.get('vol2', ""),
            'rho': request.json.get('rho', ""),
            'done': False
        }

        option_type = task['option_type']
        strike = task['strike']
        interest_rate = task['risk_free']
        maturity = task['maturity']
        a = task['a']
        b = task['b']
        spot1 = task['spot1']
        spot2 = task['spot2']
        vol1 = task['vol1']
        vol2 = task['vol2']
        rho = task['rho']
        price = pricer.MonteCarloBasket(option_type, a, b, strike, maturity, spot1, spot2, vol1, vol2, rho,
                                        interest_rate, 100.0, 10000.0)
        task['price'] = price
        task['done'] = True
        task['status'] = "Returns a price of basket option"
    elif request.json['description'] == "Best of option" or request.json['description'] == "Worst of option":
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': request.json.get('title', ""),  # ['title'],
            'description': request.json['description'],  # request.json.get('description', ""),
            'option_type': request.json['option_type'],
            'strike': request.json['strike'],
            'risk_free': request.json['risk_free'],
            'maturity': request.json['maturity'],
            'spot1': request.json.get('spot1', ""),
            'spot2': request.json.get('spot2', ""),
            'vol1': request.json.get('vol1', ""),
            'vol2': request.json.get('vol2', ""),
            'rho': request.json.get('rho', ""),
            'done': False
        }

        option_type = task['option_type']
        strike = task['strike']
        interest_rate = task['risk_free']
        maturity = task['maturity']
        spot1 = task['spot1']
        spot2 = task['spot2']
        vol1 = task['vol1']
        vol2 = task['vol2']
        rho = task['rho']
        price = pricer.MonteCarloPerf(option_type, strike, maturity, spot1, spot2, vol1, vol2, rho, interest_rate,
                                      100.0, 10000.0)
        task['price'] = price
        task['done'] = True
        task['status'] = "Returns a price of Best of or Worst of option"
    else:
        print("Bad description of option.")

    tasks.append(task)
    return jsonify({'task': make_public_task(task)}), 201


@app.route('/guy/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and \
            not isinstance(request.json['title'], six.string_types):
        abort(400)
    if 'description' in request.json and \
            not isinstance(request.json['description'], six.string_types):
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description',
                                              task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': make_public_task(task[0])})


@app.route('/guy/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
