<!DOCTYPE html>
<html>
<head>
    <title>Dicis</title>
</head>
<body>
    <h1>Dicis -Text to Speech Service</h1>
    <p>This project is a Python-based text-to-speech converter that uses the Microsoft Cognitive Services API. Given text input, it generates an audio file in mp3 format. It's designed to be simple to use, efficient, and modular.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Converts text to speech using Microsoft Cognitive Services API</li>
        <li>Allows choice of voice (RaquelNeural or FernandaNeural)</li>
        <li>Retries on failure with exponential backoff</li>
        <li>Saves audio in an organized structure</li>
    </ul>
    
    <h2>Installation</h2>
    <p>Clone the repository to your local machine:</p>
    <code>git clone https://github.com/your_username/text_to_speech_service.git</code>
    <p>Install the necessary Python packages:</p>
    <code>pip install -r requirements.txt</code>
    <p>Ensure you have the required environment variables set up:</p>
    <ul>
        <li>API_KEY : Your Microsoft Cognitive Services API key</li>
        <li>REGION : Your service region</li>
    </ul>
    <p>These can be set in a .env file in the project root:</p>
    <code>
    API_KEY=your_api_key<br>
    REGION=your_region
    </code>

    <h2>Usage</h2>
    <p>Run the main script and follow the prompts:</p>
    <code>python main.py</code>

    <h2>Contributing</h2>
    <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>
    <p>Please make sure to update tests as appropriate.</p>

    <h2>License</h2>
    <p><a href="https://choosealicense.com/licenses/mit/">MIT</a></p>

    <p>Note: You need to replace <code>https://github.com/your_username/text_to_speech_service.git</code> with the actual URL of your GitHub repository. You may also need to replace the other placeholders with your actual project details.</p>
</body>
</html>
