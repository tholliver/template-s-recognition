import json
import os
from pydub import AudioSegment

files2conver = './files2conver'


def mp3_to_wav(source, skip=0, excerpt=False):
    sound = AudioSegment.from_mp3(source)  # load source
    sound = sound.set_channels(1)  # mono
    sound = sound.set_frame_rate(16000)  # 16000Hz

    if excerpt:
        # 30 seconds - Does not work anymore when using skip
        # excrept = sound[skip*500:skip*2000+30000]
        excrept = sound
        output_path = os.path.splitext(source)[0]+"_excerpt.wav"
        print(f'The path selected: {output_path}')
        excrept.export(output_path, format="wav")
    else:
        audio = sound[skip*100:]
        output_path = os.path.splitext(source)[0]+".wav"
        audio.export(output_path, format="wav")

    return output_path


if __name__ == '__main__':
    # This code won't run if this file is imported.
    mp3_to_wav()
