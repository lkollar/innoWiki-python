#!/usr/bin/env python

from flask import Flask, jsonify, request
import datastore
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/_userlist')
def user_list():
    return jsonify(
            ID          = 1,
            Name        = "Test User",
            LoginName   = "test",
            Email       = "test@test.com"
            )

@app.route('/_getpagefromhistory', methods=['POST'])
def get_page_from_history():
    if request.method == 'POST':
        title = request.form['title']
        ds = datastore.SQLiteDataStore()
        row = ds.getHistoryPage(title)
        if ( row ):
            return jsonify(
                    ID          = row['id'],
                    Title       = row['title'],
                    Summary     = row['summary'],
                    Content     = row['content'],
                    Modified    = row['date']
                    )
        else:
            return jsonify(ID = -1)
        return
    else:
        return False

@app.route('/_getactivepage', methods=['POST'])
def get_active_page():
    if request.method == 'POST':
        title = request.form['title']
        ds = datastore.SQLiteDataStore()
        row = ds.getActivePage(title)
        if ( row ):
            return jsonify(
                    ID          = row['id'],
                    Title       = row['title'],
                    Summary     = row['summary'],
                    Content     = row['content'],
                    Modified    = row['date']
                    )
        else:
            return jsonify(ID = -1)
        return
    else:
        return False

@app.route('/_getactivepagelist')
def get_active_page():
    ds = datastore.SQLiteDataStore()
    rows = ds.getActivePageList()
    if ( rows ):
        result = []
        for row in rows:
            v = dict( ID = row['id'], 
                      Title = row['title'], 
                      Summary = row['summary'], 
                      Editor = row['editor'],
                      Modified = row['date']
                      )
            result.append(v)
        return json.dumps(result)
        
    else:
        return jsonify(ID = -1)
    return

@app.route('/_gethistorypagelistnewerthan', methods=['POST'])
def get_history_pagelist_newer_than():
    if request.method == 'POST':
        id = request.form['id']
        ds = datastore.SQLiteDataStore()
        rows = ds.getHistoryPageListNewerThan(id)
        if ( rows ):
            result = []
            for row in rows:
                v = dict( ID = row['id'], 
                          Title = row['title'], 
                          Summary = row['summary'], 
                          Editor = row['editor'],
                          Modified = row['date']
                          )
                result.append(v)
            return json.dumps(result)
            
        else:
            return jsonify(ID = -1)
        return

@app.route('/_getlasthistoryid')
def get_last_history_id():
    # TODO we should pass a cursor here instead of instantiating the datastore.
    ds = datastore.SQLiteDataStore()
    row = ds.getLastHistoryId()
    return jsonify(
            ID              = row
            )


if __name__ == '__main__':
    app.run(debug=True, port=8888)

