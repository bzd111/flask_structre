import os

from flask import Flask


def create_app(config=None):
    from . import models, routes
    app = Flask(__name__)
    models.init_app(app)
    routes.init_app(app)
    app.config.from_object('project.settings')
    if 'FLASK_CONF' in os.environ:
        print(f'FLASK_CONF: {os.environ.get("FLASK_CONF")}')
        app.config.from_envvar('FLASK_CONF')
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app


# if __name__ == '__main__':
#     app = create_app()
#     app.run(host='0.0.0.0', port=5000)
