from os import system, urandom, path, getcwd
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

def create_app():
    app = Flask(__name__,
        template_folder=path.join(getcwd(), "templates"),
        static_folder=path.join(getcwd(), "static")
    )
    app.config['SECRET_KEY'] = urandom(64)

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

    # system('rm static/*.css')
    # system('mv templates/README.html templates/index.html')

    # system('generate-md --layout jasonm23-dark --input README.md --output templates')
    # system('mv templates/assets/* static/')
    # system('rm -rf templates/assets')
    
    with app.app_context():
        from . import routes

        return app
