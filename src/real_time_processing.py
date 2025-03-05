import pyaudio
import wave
import time
import threading

class RealTimeAudioProcessor:
    def __init__(self, output_file="output.wav", duration=10, rate=44100, channels=2):
        self.output_file = output_file
        self.duration = duration
        self.rate = rate
        self.channels = channels

    def record_audio(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=1024)
        
        frames = []
        for _ in range(0, int(self.rate / 1024 * self.duration)):
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(self.output_file, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    def process_audio(self):
        print("Recording audio...")
        self.record_audio()
        print("Audio recorded and saved to", self.output_file)

if __name__ == "__main__":
    processor = RealTimeAudioProcessor()
    processor.process_audio()
