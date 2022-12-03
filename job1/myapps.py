from flask import Flask
import docker
#Connect to Docker Engine
cli = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
containers = cli.containers.list(all=True)
containers_name = ""
for i in containers:
        containers_name += i.name + ","
        print(i.name, i)
app = Flask(__name__)
#Return continers list
@app.route('/')
def list:
    return "Continers List:" + containers_name

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
