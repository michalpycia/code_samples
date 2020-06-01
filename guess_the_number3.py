from flask import Flask, request

app = Flask(__name__)
"""
    Program to play guessing game on flask server.
    Program is trying to guess the number between 1 and 1000
    User is using buttons "too small", "too big", "you win" to
    inform program about result.
    Returns:
        Guessing game located at: http://127.0.0.1:5000/ 
"""

HTML_welcome = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Choose number between 0 and 1000</title>
</head>
<body>
<h2>Choose number between 0 and 1000</h2>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="Let's play">
</form>
</body>
</html>
"""

HTML_game = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>My guess: {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="answer" value="to big">
    <input type="submit" name="answer" value="to small">
    <input type="submit" name="answer" value="you win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

HTML_winner = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Answer is {guess}</h1>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return HTML_welcome.format(0, 1000)
    else:
        current_min = int(request.form.get("min"))
        current_max = int(request.form.get("max"))
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))

        if answer == "to big":
            current_max = guess
        elif answer == "to small":
            current_min = guess
        elif answer == "you win":
            return HTML_winner.format(guess=guess)

        guess = (current_max - current_min) // 2 + current_min

        return HTML_game.format(guess=guess, min=current_min, max=current_max)


if __name__ == '__main__':
    app.run()
