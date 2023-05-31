from config import Config
from audio_saver import FileAudioSaver
from text_to_speech_service import TextToSpeechService
from voice_factory import VoiceFactory
from utils import ensure_directory_exists, get_output_path, ensure_file_exists


def main():
    output_folder = input("Please enter the output folder name: ")
    voice_number = input("Please choose the voice: 1 for RaquelNeural or 2 for FernandaNeural: ")
    voice_name = VoiceFactory.create_voice(voice_number)
    output_path = get_output_path(output_folder)

    config = Config()
    saver = FileAudioSaver()
    service = TextToSpeechService(config, saver)

    sentences_file = "sentences.txt"
    ensure_file_exists(sentences_file)

    with open(sentences_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        output_file = f"{output_path}/sentence_{i}.mp3"
        service.text_to_speech(line.strip(), output_file, voice_name, pitch="0%")

if __name__ == "__main__":
    main()
