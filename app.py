from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("processed_dataset.csv")

# Convert 'Login Time' column to datetime format
df['Login Time'] = pd.to_datetime(df['Login Time'], errors='coerce')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_time = request.form["time"]

        # Validate input time
        if not input_time.isdigit() or not (0 <= int(input_time) <= 23):
            return "Invalid time input! Please enter a number between 0 and 23."

        # Ensure 'Login Time' column is still datetime
        df['Login Time'] = pd.to_datetime(df['Login Time'], errors='coerce')

        # Drop rows where conversion failed
        df.dropna(subset=['Login Time'], inplace=True)

        # Convert input time to integer and filter doctors
        selected_doctors = df[df['Login Time'].dt.hour == int(input_time)]

        # Save filtered doctors as CSV
        selected_doctors.to_csv("selected_doctors.csv", index=False)

        return send_file("selected_doctors.csv", as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
