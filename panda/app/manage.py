# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_script.commands import ShowUrls, Clean

from app import create_app

flask_app = create_app()
manager = Manager(app=flask_app)

manager.add_command("show_urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == "__main__":
    manager.run()
