from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

def create_app():
    app = Flask(__name__)

    CORS(app)

    from api.schema import schema
    # Optional, for adding batch query support (used in Apollo-Client)
    app.add_url_rule(
        '/api/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphql_schema=schema,
            graphiql=True,
            batch=True
        )
    )
    
    with app.app_context():
        from . import routes

        return app
