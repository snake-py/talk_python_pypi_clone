import flask

from infrastructer.view_modifiers import response
import services.package_service as package_service


blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    test_packages = package_service.get_latest_packages()
    return {'package': package_name}


@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    return f'The details of the {rank} package'

