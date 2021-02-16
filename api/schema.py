from graphene import ObjectType, String, Schema, List, NonNull, Field
from mtaa import tanzania


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
    names = List(String)
    regions = list(tanzania.get_dict().keys())

    def resolve_names(root, info):
        return root.regions


class Query(ObjectType):
    hello = String(
        required=True,
        name=String(default_value='World')
    )
    tanzania = Field(Tanzania)

    def resolve_hello(parent, info, name):
        return f'Hello, {name}!'

schema = Schema(query=Query)
# schema = Schema(query=Tanzania)
