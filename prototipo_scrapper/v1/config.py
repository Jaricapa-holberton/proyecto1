#!/usr/bin/python3
"""
object to show to the sql connector which data use for connect to the database
"""
# the actual config of mysql dont need the pass option, in fact, fails if was gived in the command password :'root',
bd_connection_data = {"user" : "root", "host" :"localhost", "database" : "meli_schema"}
