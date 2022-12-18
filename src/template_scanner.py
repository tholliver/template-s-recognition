import json
import os
import numpy as np
import librosa
import scipy.spatial.distance as dist
from scipy.io import wavfile


# print(f'The file parent: {os.path.abspath(os.curdir)}')
# Ruta a los templates
templatePath = '../templates/audios'
templateDB = "../templates/templates.json"
# fullPath = os.path.abspath(os.curdir)+templatePath
# print(f'The file parent: {fullPath}')
# Data to be written
templateModel = {
    "ruta": "",
    "palabra": "",
    "specTemplate": []
}

filelist = []

# list file and directories


# # Serializing json
# json_object = json.dumps(templateModel, indent=4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)


audio_folder = './coversor/convertedFiles'
# audio_files = ["audio/agente5.wav", "audio/limpia1.wav", "audio/aula.wav",
#                "audio/aula2.wav", "audio/limpia0.wav", "audio/agente.wav"]

audio_files = os.listdir(audio_folder)  # El escaneador de archivos

data_per_templates = np.array([], dtype=object)
arrayN = []
for neighbour_fn in audio_files:
    composePath = audio_folder + '/' + neighbour_fn
    f_s, y = wavfile.read(composePath)
    n_fft = int(0.0025*f_s)      # 25 ms
    hop_length = int(0.001*f_s)  # 10 ms
    mel_spec_y = librosa.feature.melspectrogram(
        y=y/1.0, sr=f_s, n_mels=40,
        n_fft=n_fft, hop_length=hop_length
    )
    log_mel_spec_y = np.log(mel_spec_y)
    y_seq = log_mel_spec_y.T
    separator = '.'
    word_label = neighbour_fn.split(separator, 1)[0]

    data_per_templates = np.append(
        data_per_templates, {"palabra_t": word_label, "datos_spec": y_seq})
