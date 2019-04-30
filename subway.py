from flask import Flask, render_template
import random

app = Flask(__name__)


#this is the function and lists of ingredients, it will also randomize the itens to generate a new sub.
@app.route("/subway/random/")
def rand():
    #this is the list of all the ingredients of the subway
    bread = ["9 grãos", "9 grãos com aveia e mel", "italiano", "parmesão com oregano", "Tres queijos"]
    size = ["30cm", "15cm"]
    fill = ["Atum", "Beef Bacon Chipotle", "Beef Barbecue Bacon", "Carne Supreme", "BMT", "Frango", "Frango Defumado",
            "Frango Empanado", "Frango Ranch", "Frango Teriyaki", "Steak Cheddar Cremoso", "Vegetariano"]
    cheese = ["Cheddar", "Prato", "Provolone"]
    sauce = ["Mostrada e Mel", "Cebola Agridoce", "Barbecue", "Parmesão", "Chipotle", "Mostarda", "Maionese"]


    #the code bellow will select a random ingredient of the list above
    rbread = random.choice(bread)
    rsize = random.choice(size)
    rfill = random.choice(fill)
    rcheese = random.choice(cheese)
    rsauce = random.choice(sauce)

    return render_template("random.html", rbread=rbread, rsize=rsize, rfill=rfill, rcheese=rcheese, rsauce=rsauce, bread=bread, size=size, fill=fill, cheese=cheese, sauce=sauce)

#this route sets the homepage, without randomizing anything, the users must click the buttom to generate a subway
@app.route("/subway/")
def subway():
    return render_template("subway.html")

if __name__ == "__main__":
    app.run()