import flask
from infrastructer.view_modifiers import response


blueprint = flask.blueprint('account', __name__, template_folder='templates')


############ INDEX ############

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    return {}


############ REGISTER ############

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    return {}


############ LOGIN ############


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_post():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    return {}


############ LOGOUT ############


@blueprint.route('/account/logout')
@response(template_file='account/logout.html')
def logout():
    return {}
