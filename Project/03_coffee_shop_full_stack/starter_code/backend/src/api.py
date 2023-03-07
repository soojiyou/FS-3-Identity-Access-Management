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
    req_title = request.json.get('title')
    req_recipe = request.json.get('recipe')
    requested_drink = Drink.query.get(id)
    if not requested_drink:
        abort(404)

    try:
        if req_title:
            requested_drink.title = req_title

        if req_recipe:
            requested_drink.recipe = req_recipe

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


# import os
# from flask import Flask, request, jsonify, abort
# from sqlalchemy import exc
# import json
# from flask_cors import CORS

# from database.models import db_drop_and_create_all, setup_db, Drink
# from auth.auth import AuthError, requires_auth

# app = Flask(__name__)
# setup_db(app)
# CORS(app)

# '''
# @TODO uncomment the following line to initialize the datbase
# !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
# !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
# '''
# db_drop_and_create_all()

# # ROUTES
# '''
# @TODO implement endpoint
#     GET /drinks
#         it should be a public endpoint
#         it should contain only the drink.short() data representation
#     returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
#         or appropriate status code indicating reason for failure
# '''


# @app.route('/drinks', methods=['GET'])
# def get_drinks():
#     if request.method == "GET":
#         all_drinks = Drink.query.all()
#         drinks = [drink.short() for drink in all_drinks]
#         return jsonify({
#             'success': True,
#             'drinks': drinks
#         }), 200


# '''
# @TODO implement endpoint
#     GET /drinks-detail
#         it should require the 'get:drinks-detail' permission
#         it should contain the drink.long() data representation
#     returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
#         or appropriate status code indicating reason for failure
# '''


# @app.route('/drinks-detail', methods=['GET'])
# @requires_auth('get:drinks-detail')
# def get_drinks_detail(payload):
#     if request.method == "GET":
#         all_drinks = Drink.query.all()
#         drinks = [drink.long() for drink in all_drinks]
#         return jsonify({
#             'success': True,
#             'drinks': drinks
#         }), 200


# '''
# @TODO implement endpoint
#     POST /drinks
#         it should create a new row in the drinks table
#         it should require the 'post:drinks' permission
#         it should contain the drink.long() data representation
#     returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
#         or appropriate status code indicating reason for failure
# '''


# @app.route('/drinks', methods=['POST'])
# @requires_auth('post:drinks')
# def post_drink(payload):
#     # if the method is POST
#     if request.method == "POST":
#         # get the data
#         body = request.get_json()
#         print(body)
#         try:
#             recipe = body['recipe']
#             if type(recipe) is dict:
#                 recipe = [recipe]

#             title = body['title']
#             # create an instance and serialize recipe to str
#             drink = Drink(title=title, recipe=json.dumps(recipe))
#             drink.insert()
#             drinks = [drink.long()]

#             return jsonify({
#                 'success': True,
#                 'drinks': drinks
#             })

#         except:
#             abort(422)


# '''
# @TODO implement endpoint
#     PATCH /drinks/<id>
#         where <id> is the existing model id
#         it should respond with a 404 error if <id> is not found
#         it should update the corresponding row for <id>
#         it should require the 'patch:drinks' permission
#         it should contain the drink.long() data representation
#     returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
#         or appropriate status code indicating reason for failure
# '''


# @app.route('/drinks/<int:drink_id>', methods=['PATCH'])
# @requires_auth('patch:drinks')
# def patch_drink(payload, drink_id):
#     if request.method == "PATCH":
#         body = request.get_json()
#         print(body)

#         drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
#         if not drink:
#             abort(404)

#         try:
#             title = body.get('title', None)

#             recipe = body.get('recipe', None)

#             if title != None:
#                 drink.title = title

#             if recipe != None:
#                 drink.recipe = json.dumps(body['recipe'])

#             drink.update()

#             drinks = [drink.long()]

#             return jsonify({
#                 'success': True,
#                 'drinks': drinks
#             }), 200

#         except:
#             abort(422)


# '''
# @TODO implement endpoint
#     DELETE /drinks/<id>
#         where <id> is the existing model id
#         it should respond with a 404 error if <id> is not found
#         it should delete the corresponding row for <id>
#         it should require the 'delete:drinks' permission
#     returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
#         or appropriate status code indicating reason for failure
# '''


# @app.route('/drinks/<int:drink_id>', methods=['DELETE'])
# @requires_auth('delete:drinks')
# def delete_drink(payload, drink_id):
#     if request.method == "DELETE":
#         drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

#         if not drink:
#             abort(404)

#         try:
#             drink.delete()
#             return jsonify({
#                 'success': True,
#                 'delete': drink.id
#             }), 200
#         except:
#             abort(422)


# # Error Handling
# '''
# Example error handling for unprocessable entity
# '''
# '''
# @TODO implement error handlers using the @app.errorhandler(error) decorator
#     each error handler should return (with approprate messages):
#              jsonify({
#                     "success": False,
#                     "error": 404,
#                     "message": "resource not found"
#                     }), 404
# '''


# @app.errorhandler(400)
# def bad_request(error):
#     return jsonify({
#         'success': False,
#         'error': 400,
#         'message': 'Bad Request'
#     }), 400


# @app.errorhandler(401)
# def unauthorized(error):
#     return jsonify({
#         'success': False,
#         'error': 401,
#         'message': 'Unauthorized'
#     }), 401


# '''
# @TODO implement error handler for 404
#     error handler should conform to general task above
# '''


# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({
#         'success': False,
#         'error': 404,
#         'message': 'Not Found'
#     }), 404


# @app.errorhandler(405)
# def method_not_allowed(error):
#     return jsonify({
#         'success': False,
#         'error': 405,
#         'message': 'Method Not Allowed'
#     }), 405


# @app.errorhandler(422)
# def unprocessable(error):
#     return jsonify({
#         "success": False,
#         "error": 422,
#         "message": "Unprocessable"
#     }), 422


# @app.errorhandler(500)
# def internal_server_error(error):
#     return jsonify({
#         'success': False,
#         'error': 500,
#         'message': 'Internal Server Error'
#     }), 500


# '''
# @TODO implement error handler for AuthError
#     error handler should conform to general task above
# '''


# @app.errorhandler(AuthError)
# def auth_error(error):
#     return jsonify({
#         'success': False,
#         'error': error.status_code,
#         'message': error.error['description']
#     }), error.status_code
