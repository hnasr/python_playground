import tornado.web
import tornado.ioloop
import psycopg2
import json

#define connection variable (state)
con = None

class getHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("stateful.html")

class connectHandler(tornado.web.RequestHandler):
    def post(self):
        #connect to the db 
        global con
        con = psycopg2.connect(
                host = "husseinmac",
                database="husseindb",
                user = "postgres",
                password = "postgres")

 
        self.set_header("content-type", "application/json")
        self.write(json.dumps({"success": True}))

class readHandler(tornado.web.RequestHandler):
    def post(self):
        global con
        try:
            #cursor 
            cur = con.cursor()

            #execute query
            cur.execute("select id, name from profiles where id = 362")

            rows = cur.fetchall()

            #close the cursor
            cur.close()
            
            #close the connection
            self.set_header("content-type", "application/json")
            self.write(json.dumps(rows[0]))
        except: 
            self.write(json.dumps({"success": False, "error": "Failed read the database."}))

    def get(self):
        self.render("stateless.html")

class closeHandler(tornado.web.RequestHandler):
    def post(self):
        global con

        self.set_header("content-type", "application/json")
        try:
            #close the connection
            con.close()
            self.write(json.dumps({"success": True}))
        except: 
            self.write(json.dumps({"success": False, "error": "Failed to close database."}))

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/stateful", getHandler),
        ("/stateful/connect", connectHandler),
        ("/stateful/read", readHandler),
        ("/stateful/close", closeHandler)
    ])

    app.listen(3000)
    print("Listening on port 3000")
    tornado.ioloop.IOLoop.instance().start()