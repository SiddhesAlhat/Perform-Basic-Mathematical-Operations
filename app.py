from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Basic validation
        if not name or not email or not password:
            return "All fields are required!"

        return render_template(
            "success.html",
            name=name,
            email=email
        )

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
