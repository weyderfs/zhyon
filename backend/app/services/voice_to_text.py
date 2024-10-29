# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = ""

# URL of the file to transcribe
# FILE_URL = "https://assemblyaiusercontent.com/playground/44wJ7_1D12x.m4a"

# You can also transcribe a local file by passing in a file path
FILE_URL = "./test.m4a"

# You can set additional parameters for the transcription
config = aai.TranscriptionConfig(
  speech_model=aai.SpeechModel.best,
  speaker_labels=True,
  language_detection=True
)

transcriber = aai.Transcriber(config=config)
transcript = transcriber.transcribe(FILE_URL)
utterances = transcript.utterances

result_output = ""

for utterance in utterances:
  speaker = utterance.speaker
  text = utterance.text
  result_output = f"{result_output}Speaker {speaker}: {text}\n"

file = open("file.txt", "w")
file.write(result_output)
file.close()
