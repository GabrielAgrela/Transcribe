# Dicis - Text to Speech Service

This project is a Python-based text-to-speech converter that uses the Microsoft Cognitive Services API. Given text input file, it generates audio files in mp3 format. It's designed to be simple to use, efficient, and modular.

## Features

- Converts text to speech using Microsoft Cognitive Services API
- Allows choice of voice (RaquelNeural or FernandaNeural)
- Retries on failure with exponential backoff
- Saves audios in an organized structure

## Installation

Clone the repository to your local machine:

git clone https://github.com/GabrielAgrela/Dicis.git

Install the necessary Python packages:

pip install -r requirements.txt

Ensure you have the required environment variables set up:

- `API_KEY` : Your Microsoft Cognitive Services API key
- `REGION` : Your service region

These can be set in a `.env` file in the project root:

API_KEY=your_api_key
REGION=your_region

## Usage

Run the main script and follow the prompts:

python main.py

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
