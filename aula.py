
from Flask import Flask

app = Flask (__name__)
@app.route('/')
#essa '/' é para chamar a função def --# sempre por antes da função a '/' 
def hello_word():
    return 'Hello,word!'

if _name_ == '_main_':
        app;run(port=5001)