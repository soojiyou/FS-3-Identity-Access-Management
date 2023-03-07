import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from database.models import db_drop_and_create_all, setup_db, Drink
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    if not drinks:
        return abort(404)

    for drink in drinks:
        drink_short = drink.short()

    return jsonify({
        "success": True,
        "drinks": [drink_short],
    }), 200


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


# @app.route('/drinks-detail', methods=['GET'])
# @requires_auth('get:drinks-detail')
# def get_drinks_detail(payload):
#     drinks = Drink.query.all()
#     for drink in drinks:
#         drink_long = drink.long()
#     if not drinks:
#         return abort(404)

#     return jsonify({
#         "success": True,
#         "drink": [drink_long],
#     }), 200


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    drinks = Drink.query.all()
    if not drinks:
        return abort(404)
    for drink in drinks:
        drink_long = drink.long()
    # drinks_long = [drink.long() for drink in drinks]

    return jsonify({
        'success': True,
        'drinks': [drink_long]
    })


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(payload):
    new_title = request.json.get('title')
    new_recipe = request.json.get('recipe')

    if not new_title and new_recipe:
        abort(400)
    try:
        # if type(new_recipe) is dict:
        #     new_recipe = [new_recipe]

        post_drink = Drink(title=new_title, recipe=json.dumps(new_recipe))
        post_drink.insert()

        # for drink in post_drink:
        #     drink_long = drink.long()

        drink_long = post_drink.long()
        return jsonify({
            "success": True,
            "drinks": [drink_long],
        }), 200
    except:
        abort(422)


# FFF0DF
# 4D331A
'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(pqyload, id):
    requested_drink = Drink.query.get(id)
    if not requested_drink:
        abort(404)

    req_title = request.json.get('title')
    req_recipe = request.json.get('recipe')
    if not req_title or not req_recipe:
        abort(400)

    try:
        if req_title:
            requested_drink.title = req_title

        if req_recipe:
            requested_drink.recipe = json.dumps(req_recipe)

        requested_drink.update()

        drink_long = requested_drink.long()
        return jsonify({
            'success': True,
            'drinks': [drink_long],
        }), 200

    except Exception:
        abort(422)


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    target_drink = Drink.query.get(id)
    if not target_drink:
        abort(404)

    try:
        target_drink.delete()

        return jsonify({
            'success': True,
            'delete': id,
        }), 200

    except Exception:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False,
                    "error": 404,
                    "message": "Not found"}), 404


@ app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify({"success": False,
                 "error": 422,
                 "message": "unprocessable"}), 422
    )


@ app.errorhandler(400)
def bad_request(error):
    return jsonify({"success": False,
                    "error": 400,
                    "message": "bad request"}), 400


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def not_authenticated(auth_error):
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": auth_error.error
    }), 401
