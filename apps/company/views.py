from flask import Blueprint
from flask_restful import Api

from apps.company.resources.search import SearchCompanyResource
from apps.company.resources.tag import CompanyTagListResource, CompanyTagResource

blueprint = Blueprint('api', __name__, url_prefix='/v1')
api = Api(blueprint)

api.add_resource(CompanyTagListResource, '/companies/<int:company_id>/tags')
api.add_resource(CompanyTagResource, '/companies/<int:company_id>/tags/<int:tag_id>')
api.add_resource(SearchCompanyResource, '/search/companies')
