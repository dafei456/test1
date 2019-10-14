from application import app, manager
from flask_script import Server
import www

manager.add_command("runserver", Server(host="0.0.0.0",
                                        port=app.config['SERVER_PORT'],
                                        use_debugger=app.config['DEBUG']))


def main():
    manager.run()


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()