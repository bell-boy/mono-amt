import verovio
import tqdm
import random
import mido
import midi2audio

tk = verovio.toolkit()
verovio.enableLog(verovio.LOG_OFF)
num_examples = 90_000

m2a = midi2audio.FluidSynth("flute.SF2")


with open("data/transcripts.txt", "r") as f:
    idx = 0
    for i in tqdm.tqdm(range(num_examples)):
        next_line = f.readline()

        if tk.loadData(next_line):
            tk.renderToMIDIFile(f"data/midifiles/{idx}.midi")
            """
            midifile = mido.MidiFile(f"data/midifiles/{idx}.midi")
            tempo = random.randint(80, 144)
            for track in midifile.tracks:
                for msg in track:
                    if msg.type == "set_tempo":
                        msg.tempo = tempo
            midifile.save(f"data/midifiles/{idx}.midi")
            """
            m2a.midi_to_audio(f"data/midifiles/{idx}.midi", f"data/audiofiles/{idx}.wav")
            idx += 1    

