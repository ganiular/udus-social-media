from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('forums')
def forums():
    return {
        "Category 1": [{'id':1, 'name':'Forum 1'}, {'id':2, 'name':'Forum 2'}, {'id':3, 'name':'Forum 3'}],
        "Category 2": [{'id':1, 'name':'Forum 1'}, {'id':2, 'name':'Forum 2'}, {'id':3, 'name':'Forum 3'}],
        "Category 3": [{'id':1, 'name':'Forum 1'}, {'id':2, 'name':'Forum 2'}, {'id':3, 'name':'Forum 3'}],
        "Category 4": [{'id':1, 'name':'Forum 1'}, {'id':2, 'name':'Forum 2'}, {'id':3, 'name':'Forum 3'}],
        "Category 5": [{'id':1, 'name':'Forum 1'}, {'id':2, 'name':'Forum 2'}, {'id':3, 'name':'Forum 3'}],
    }

