from flask.ext.script import Command

class Demo(Command):
    """
        prints hello world
    """

    def run(self):
        print "hello world"
