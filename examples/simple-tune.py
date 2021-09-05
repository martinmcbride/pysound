from pysound import buffer
from pysound import soundfile
from pysound import oscillators
from pysound import envelopes
from pysound import mixers
from pysound import const

def simple_instr(params, frequency):
    env = envelopes.attack_decay(params, attack=params.t2s(0.05))
    tone = oscillators.saw_wave(params, frequency=frequency, amplitude=env)
    return tone

params = buffer.BufferParams().with_duration(7)
beatp = buffer.BufferParams(params).with_duration(1)
beat = beatp.length;
data = mixers.sequencer(params,
                        [(simple_instr(beatp, const.Notes.C4), 0),
                         (simple_instr(beatp, const.Notes.D4), beat),
                         (simple_instr(beatp, const.Notes.E4), beat*2),
                         (simple_instr(beatp, const.Notes.F4), beat*3),
                         (simple_instr(beatp, const.Notes.G4), beat*4),
                         (simple_instr(beatp, const.Notes.A4), beat*5),
                         (simple_instr(beatp, const.Notes.B4), beat*6),
                         ])
soundfile.save(params, '/tmp/test.wav', data)
