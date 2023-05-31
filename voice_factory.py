class VoiceFactory:
    @staticmethod
    def create_voice(voice_number):
        return 'pt-PT-RaquelNeural' if voice_number == '1' else 'pt-PT-FernandaNeural'
