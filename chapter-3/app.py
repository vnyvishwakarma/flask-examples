
from flask import Flask, render_template

app = Flask(__name__)

employees_list = [
    {
        'name': 'Vinay Kr. Vishwakarma',
        'title': 'Devops Expert',
        'company': 'The Dock'
    },
    {
        'name': 'Pankaj Sharma',
        'title': 'Devops Specialist',
        'company': 'Vodafone'
    },
    {
        'name': 'Mayank Koli',
        'title': 'Devops Specialist',
        'company': 'Airtel'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', employees=employees_list)
    

if __name__ == '__main__':
    app.run(debug=True)