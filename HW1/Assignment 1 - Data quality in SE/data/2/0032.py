# coding: utf-8

import sys

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_assets import ManageAssets

from app import app
from assets import assets
from db import db

from .changepassword import ChangePassword
from .create_superuser import SuperUserCommand
from .scaffold import ScaffoldingCommand
from .upload_static_files import UploadStaticFiles


class MyMan(Manager):
    def run(self, commands=None, default_command=None):
        """
        Prepares manager to receive command line input. Usually run
        inside "if __name__ == "__main__" block in a Python script.

        :param commands: optional dict of commands. Appended to any commands
                         added using add_command().

        :param default_command: name of default command to run if no
                                arguments passed.
        """

        if commands:
            self._commands.update(commands)

        if default_command is not None and len(sys.argv) == 1:
            sys.argv.append(default_command)

        try:
            result = self.handle(sys.argv[0], sys.argv[1:])
        except SystemExit as e:
            result = e.code
            sys.exit(result or 0)


man = MyMan(app)
man.add_command('db', MigrateCommand)

migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)
manager.add_command('create_superuser', SuperUserCommand())
manager.add_command('upload_static_files', UploadStaticFiles())
manager.add_command('change_password', ChangePassword())
manager.add_command('scaffold', ScaffoldingCommand())
manager.add_command("assets", ManageAssets(assets))
