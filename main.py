from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

item_put_args = reqparse.RequestParser()
item_put_args.add_argument("name", type=str, help="Name of the item is required", required=True)
item_put_args.add_argument("price", type=float, help="Price of the item is required", required=True)




items = {}

def abort_if_item_id_doesnt_exist(item_id):
    if item_id not in items:
        abort(404, message="item id is not valid...")

def abort_if_item_exists(item_id):
    if item_id in items:
        abort(409, message="Item already exist with that ID...")

class Item(Resource):
    def get(self, item_id):
        abort_if_item_id_doesnt_exist(item_id)
        return items[item_id]

    def put(self, item_id):
        abort_if_item_exists(item_id)
        args = item_put_args.parse_args()
        items[item_id] = args
        return items[item_id], 201

    def delete(self, item_id):
        abort_if_item_id_doesnt_exist(item_id)
        del items[item_id]
        return "",204


api.add_resource(Item, "/item/<int:item_id>")

if __name__ == "__main__":
    app.run(debug=True)