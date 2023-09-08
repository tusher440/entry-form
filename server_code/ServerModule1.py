import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def submit(name, weight, address, training):
  app_tables.form.add_row(name=name, weight=weight, address=address, training=training)
  anvil.email.send(from_name='My App Support',
                  to='abirhossaintushar.789@gmail.com',
                  subject='Wellcome',
                  text=f"name from {name}: weight from {weight}: live in {address}: training at {training}"
                  )