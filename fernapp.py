from flask import Flask, request, redirect
import sh
from time import sleep

app = Flask(__name__)

@app.route("/")
def root():
    if request.method == 'GET' and 'path' in request.args:
        try:
            sh.killall('java')
        except:
            pass
        command = sh.Command('/home/libreoffice/Projects/fernapp-server.sh')
        result = command('soffice', request.args['path'], _bg=True)
        print(result.ran)
        sleep(8)
        return redirect('http://libreoffice.havana.in:8080')
    else:
        return "Path to file please"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
