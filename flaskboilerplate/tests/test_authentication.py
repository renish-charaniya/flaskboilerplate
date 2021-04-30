from flask import Flask


try:
    from run import app
    import unittest

except Exception as e:
    print("Some Modules are missing {}",format(e))

def test_base_routes():
    app=Flask(__name__)
    configure_routes(app)