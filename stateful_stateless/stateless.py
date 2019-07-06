import tornado.web
import tornado.ioloop
import psycopg2
import json

class getHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("stateless.html")

class statelessHandler(tornado.web.RequestHandler):
    def post(self):
        #connect to the db 
        con = psycopg2.connect(
                host = "husseinmac",
                database="husseindb",
                user = "postgres",
                password = "postgres")

        #cursor 
        cur = con.cursor()

        #execute query
        cur.execute("select id, name from profiles where id = 362")

        rows = cur.fetchall()

        #close the cursor
        cur.close()

        #close the connection
        con.close()
        self.set_header("content-type", "application/json");
        self.write(json.dumps(rows[0]))

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/stateless", getHandler),
        ("/stateless/read", statelessHandler)
    ])

    app.listen(2000)
    print("Listening on port 2000")
    tornado.ioloop.IOLoop.instance().start()