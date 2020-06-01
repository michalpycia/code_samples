from flask import Flask, request

app = Flask(__name__)


def celfahr(celcius):
    return 2 * celcius + 32


def fahrcel(fahrenheit):
    return (fahrenheit - 32) // 2


index = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Temperature converter</title>
</head>
<body>
<h2>Temperature converter</h2>
<form  action="" method="POST">
  <input type="number" name="temperature"></input>
  <input type="submit" value="Calculate"><br>
  <input type="radio" name="calc" value="Celcius to Fahrenheit">
  <label">Celcius to Fahrenheit</label><br>
  <input type="radio" name="calc" value="Z Fahrenheit to Celcius">
  <label>Fahrenheit to Celcius</label><br>

  
  
</form>
</body>
</html>
"""

indexa = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Temperature converter</title>
</head>
<body>
<h2>Temperature converter</h2>
<form  action="" method="POST">
<input type="number" name="temperature"></input>
  <input type="submit" value="Calculate"><br>
  <input type="radio"  name="calc" value="Celcius to Fahrenheit">
  <label for="celcfahr">Celcius to Fahrenheit</label><br>
  <input type="radio"  name="calc" value="Fahrenheit to Celcius">
  <label for="fahrcelc">Fahrenheit to Celcius</label><br>
  <h3>{temperature} {choosen} is {result} {choosen2}</h3>

</form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def temperature():
    """
    Temperature converter based on Flask server.
    Returns:
        HTML temperature converter on http://127.0.0.1:5000/
    """
    if request.method == "GET":
        return index
    else:
        user_choice = (request.form.get("calc"))
        temperature = int((request.form.get("temperature")))

        if user_choice == "Celcius to Fahrenheit":
            choosen = 'Celcius'
            choosen2 = 'Fahreint'
            result = celfahr(temperature)
        else:
            choosen = 'Fahreint'
            choosen2 = 'Celcius'
            result = fahrcel(temperature)

        return indexa.format(result=result, choosen=choosen, choosen2=choosen2, temperature=temperature)


if __name__ == '__main__':
    app.run()
