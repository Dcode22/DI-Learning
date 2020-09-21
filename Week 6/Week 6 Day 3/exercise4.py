from flask import Flask, render_template
app = Flask(__name__)

@app.route('/cv')
def createcv():
    name = "Dovid Levine"
    image = "https://dovidylevine.com/thedave.jpg"
    hobbies = "drawing, guitar, reading"
    skills = "programming, English, organization"
    strengths = "drive, intelligence" 
    weaknesses = "people skills, balance"

    return render_template("cv.html", name= name, image = image, hobbies = hobbies, skills = skills, strengths = stregths, weakenesses = weaknesses )

app.run(debug= True)
