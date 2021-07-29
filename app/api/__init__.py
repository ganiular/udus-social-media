from flask import Blueprint, request

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

@bp.route('forum/<int:fid>/<forum_name>')
def forum_posts(fid, forum_name):
    max_len = request.args.get('length', 20)
    nextof = request.args.get('nextof', 0)
    return {
        'forum_name': forum_name,
        'posts': ( 
            {'pid':5, 'uid':1, 'author':'Quadri Ganiu Olawale', 'date':'08-10-2020', 'text':'hello world'},
            {'pid':5, 'uid':1, 'author':'Quadri Ganiu Olawale', 'date':'08-10-2020', 'text':'hello world'},
            {'pid':5, 'uid':1, 'author':'Quadri Ganiu Olawale', 'date':'08-10-2020', 'text':'hello world'},
            {'pid':5, 'uid':1, 'author':'Quadri Ganiu Olawale', 'date':'08-10-2020', 'text':'hello world'},
            {'pid':5, 'uid':1, 'author':'Quadri Ganiu Olawale', 'date':'08-10-2020', 'text':'hello world'},
        ),
    }
