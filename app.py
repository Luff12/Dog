from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/dog')
def dog():
    # Fetch a random dog image from the Dog CEO API
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_data = response.json()
    
    # Check if the response is successful
    if dog_data['status'] == 'success':
        dog_image_url = dog_data['message']
    else:
        dog_image_url = None
    
    return render_template('dog.html', dog_image=dog_image_url)

@app.route('/')
def index():
    return redirect(url_for('dog'))

if __name__ == '__main__':
    app.run(debug=True)
