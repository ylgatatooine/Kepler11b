""" 
Leverage Google Video Intelligence service to transcribe from a video or audio files stored on Google Cloud Storage. 
1. Google Cloud active project. 
2. Store the video or audio file on Google Cloud Storage
3. Run, e.g. Google Cloud Shell Editor and ipython. 

Todo: Check out Llama models 
"""


from google.cloud import videointelligence

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.SPEECH_TRANSCRIPTION]
# path
file_gs_uri = "gs://lianggang-video-intel/GettysburgeAddress.mp4" 
lang_in_video = "en-US"

config = videointelligence.SpeechTranscriptionConfig(
    language_code=lang_in_video, enable_automatic_punctuation=True
)
video_context = videointelligence.VideoContext(speech_transcription_config=config)

operation = video_client.annotate_video(
    request={
        "features": features,
        "input_uri": file_gs_uri,
        "video_context": video_context,
    }
)

print("\nProcessing for the transcription ... ")

result = operation.result(timeout=300)
# Keep it simple for the demo. One file and one annotation.
annotation = result.annotation_results[0]

for speech_transcription in annotation.speech_transcriptions:

    # The number of alternatives for each transcription is limited by
    # SpeechTranscriptionConfig.max_alternatives.
    for alternative in speech_transcription.alternatives:
        print("".format(alternative.transcript))
