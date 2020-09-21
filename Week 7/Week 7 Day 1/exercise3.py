from flask import Flask
import random
app = Flask(__name__)

@app.route('/<int:number>')
def randmatch(number):
    random_number = random.randint(1, 101)

    if random_number == number:
        return f"success your number: {number} was right!"
    
    return f"your number {number} did not match {random_number}"

app.run(debug= True)

# exercise 4

