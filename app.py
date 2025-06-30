from flask import Flask, render_template, request
import serial
import time

# Replace 'COM3' with your actual Arduino port
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    try:
        angle1 = request.form['angle1']
        angle2 = request.form['angle2']
        angle3 = request.form['angle3']
        angle4 = request.form['angle4']
        
        command = f"{angle1} {angle2} {angle3} {angle4}\n"
        print(f"Sending to Arduino: {command.strip()}")
        arduino.write(command.encode())
        return "OK"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allows access from other devices
