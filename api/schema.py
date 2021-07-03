from graphene import ObjectType, String, Schema, List, NonNull, Field
from mtaa import tanzania
import mtaa


class Street(ObjectType):
    names = List(String)


class Ward(ObjectType):
    post_code = String(required=True)
    streets = List(Street)


class District(ObjectType):
    post_code = String(required=True)
    wards = List(Ward)


class Region(ObjectType):
    post_code = String(required=True)
    districts = List(District)


class Tanzania(ObjectType):
    regions = List(String)
    districts = List(String)
    wards = List(String)
    streets = List(String)

    def resolve_regions(root, info):
        return mtaa.regions

    def resolve_districts(root, info):
        return mtaa.districts

    def resolve_wards(root, info):
        return mtaa.wards

    def resolve_streets(root, info):
        return mtaa.streets


class Query(ObjectType):
    hello = String(
        required=True,
        #  name=String(default_value='World')
    )
    tanzania = Field(Tanzania)

    def resolve_hello(parent, info, name):
        return f'Hello, {name}!'


schema = Schema(query=Query)
