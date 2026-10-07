from flask import redirect, request, url_for
from splent_framework.app_factory import create_splent_app


def create_app(config_name=None):
    # No profile named: the framework follows SPLENT_ENV (dev, prod, test).
    app = create_splent_app(__name__, config_name)
    app.jinja_env.globals["ruta_existe"] = lambda nombre: nombre in app.view_functions
    if getattr(app, "login_manager", None):
        app.login_manager.login_message = None

    @app.before_request
    def inicio_en_tareas():
        if request.path == "/" and "planner_tasks.tareas" in app.view_functions:
            return redirect(url_for("planner_tasks.tareas"))

    return app
