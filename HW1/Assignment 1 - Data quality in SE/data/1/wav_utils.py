import os
import wave
import numpy
import struct
import tempfile
import matplotlib.pyplot as plt

try:
    import pyaudio
except:
    pyaudio = None


class Wave:
    def __init__(self, samples, sample_rate):
        self.sample_rate = sample_rate
        self.samples = samples

    def save(self, filename):
        output_file = wave.open(filename, 'w')
        output_file.setparams((1, 2, self.sample_rate, 0, 'NONE', 'not compressed'))

        out = []
        for frame in self.samples:
            frame = max(-1, min(1, frame))
            frame = int(frame * (2**15 - 1))
            out.append(frame)

        output_file.writeframes(b''.join(struct.pack('<h', frame)
                                         for frame in out))
        output_file.close()

    def plot(self, show=True):
        """
        Open a matplotlib window showing the contents of the given wav file
        """
        xs, ys = zip(*[(float(ix)/self.sample_rate, val)
                       for ix, val in enumerate(self.samples)])
        plt.plot(xs, ys)
        if show:
            plt.show()

    def play(self):
        """
        REQUIRES PYAUDIO TO BE INSTALLED
        """
        assert pyaudio is not None, ("You need to have pyaudio installed to "
                                     "use the play_wav function")
        filename = os.path.join(tempfile.gettempdir(),
                                '6003_wave_%s.wav' % abs(hash(tuple(self.samples))))
        self.save(filename)
        f = wave.open(filename, 'r')
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)

            data = f.readframes(10240)
            while data:
                stream.write(data)
                data = f.readframes(10240)

            stream.stop_stream()
            stream.close()
            p.terminate()
        finally:
            f.close()
            os.unlink(filename)

    @classmethod
    def from_file(cls, filename):
        """
        Read a wave file.  This will always convert to mono.

        Returns a tuple with 2 elements:
          * a Python list with floats [-1, 1] representing samples
          * an integer containing the sample rate
        """
        f = wave.open(filename, 'r')
        chan, bd, sr, count, _, _ = f.getparams()

        assert bd == 2, "bit depth must be 16"

        data = []
        for i in range(count):
            frame = f.readframes(1)
            if chan == 2:
                l = struct.unpack('<h', frame[:2])[0]
                r = struct.unpack('<h', frame[2:])[0]
                datum = (l + r) / 2
            else:
                datum = struct.unpack('<h', frame)[0]
            data.append(datum)

        if chan == 2:
            # if stereo, convert to mono
            data = [(data[2*i]+data[2*i+1])/2 for i in range(count//2)]

        return cls([i/2**15 for i in data], sr)
