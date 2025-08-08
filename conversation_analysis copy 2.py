from utils.stt import transcribe_audio
from utils.diarization import diarize_audio
from utils.summarization import summarize_file

def conversation_analysis_page():
    st.header("Conversation Analysis")
    audio_file = st.file_uploader("Upload Audio (wav/mp3)", type=["wav", "mp3"])
    if audio_file:
        with st.spinner("Transcribing audio..."):
            transcript_data = transcribe_audio(audio_file)  # dict with 'text'

        transcript_text = transcript_data.get('text', transcript_data) if isinstance(transcript_data, dict) else transcript_data
        st.subheader("Transcript")
        st.text_area("", transcript_text, height=200)

        with st.spinner("Performing diarization..."):
            diarized_text = diarize_audio(audio_file)  # returns diarization with timestamps/speakers

        st.subheader("Diarized Transcript")
        st.text_area("", diarized_text, height=200)

        with st.spinner("Summarizing transcript..."):
            summary = summarize_file(transcript_text)

        st.subheader("Summary")
        st.write(summary)
