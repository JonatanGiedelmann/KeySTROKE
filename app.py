from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def analyze_typing_data(typing_data):
    intervals = []
    keypress_intervals = {}

    for i in range(1, len(typing_data)):
        if typing_data[i]['eventType'] == 'keydown' and typing_data[i-1]['eventType'] == 'keyup':
            interval = typing_data[i]['timestamp'] - \
                typing_data[i-1]['timestamp']
            intervals.append(interval)

            key = typing_data[i-1]['key']
            if key not in keypress_intervals:
                keypress_intervals[key] = []
            keypress_intervals[key].append(interval)

    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    keypress_avg_intervals = {k: sum(v) / len(v)
                              for k, v in keypress_intervals.items()}

    return {
        'average_interval': avg_interval,
        'keypress_intervals': keypress_avg_intervals
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    typing_data = request.json['typingData']
    behavioral_signature = analyze_typing_data(typing_data)
    return jsonify(behavioral_signature)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
