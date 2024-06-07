<!DOCTYPE html>
<html>

<head>
    <title>Typing Behavior Analyzer</title>
    <style>
        #inputArea {
            width: 100%;
            height: 100px;
            font-size: 16px;
        }
    </style>
</head>

<body>
    <h1>Typing Behavior Analyzer</h1>
    <p>Start typing in the text area below:</p>
    <textarea id="inputArea" placeholder="Start typing..."></textarea>
    <button onclick="sendData()">Analyze</button>

    <script>
        let typingData = [];

        document.getElementById('inputArea').addEventListener('keydown', (event) => {
            let timestamp = new Date().getTime();
            typingData.push({
                key: event.key,
                timestamp: timestamp,
                eventType: 'keydown'
            });
        });

        document.getElementById('inputArea').addEventListener('keyup', (event) => {
            let timestamp = new Date().getTime();
            typingData.push({
                key: event.key,
                timestamp: timestamp,
                eventType: 'keyup'
            });
        });

        function sendData() {
            fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ typingData: typingData })
            })
                .then(response => response.json())
                .then(data => {
                    alert('Behavioral signature generated:\n' + JSON.stringify(data));
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    </script>
</body>

</html>
