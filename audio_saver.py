from abc import ABC, abstractmethod

class AudioSaver(ABC):
    @abstractmethod
    def save(self, content, output_file):
        pass

class FileAudioSaver(AudioSaver):
    def save(self, content, output_file):
        with open(output_file, "wb") as f:
            f.write(content)
        print(f"Saved to {output_file}")
