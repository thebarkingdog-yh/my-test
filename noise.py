import asyncio
import io
import sys
import wave

import pyaudio
import redis.asyncio as redis

r = redis.Redis(host="192.168.1.78", port=6379, db=0)
AUDIO_IN_CHANNEL = "audio:in"
AUDIO_OUT_CHANNEL = "audio:out"
CHUNK = 2048

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1 if sys.platform == "darwin" else 2,
    rate=44100,
    input=True,
    output=True,
)


def convert_to_wav(frames, sample_width, channels, sample_rate):
    wav_file = io.BytesIO()

    with wave.open(wav_file, "wb") as wave_writer:
        wave_writer.setnchannels(channels)
        wave_writer.setsampwidth(sample_width)
        wave_writer.setframerate(sample_rate)
        wave_writer.writeframes(b"".join(frames))

    wav_data = wav_file.getvalue()
    wav_file.close()

    return wav_data


def convert_wave_to_bytes(wave_data):
    w = io.BytesIO(wave_data)
    with wave.open(w, "rb") as wave_reader:
        data = wave_reader.readframes(wave_reader.getnframes())

    return data


async def reader(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            channel_name = message.get("channel").decode("utf-8")
            data = message.get("data")

            if channel_name == AUDIO_IN_CHANNEL:
                # remove noise of audio from dog_ai_server
                # ...

                # wav = convert_to_wav([data], 2, 1, 44100)
                # b = convert_wave_to_bytes(wav)
                # stream.write(b)
                stream.write(data)

            elif channel_name == AUDIO_OUT_CHANNEL:
                # play audio
                # print("play audio:", len(data), "bytes")
                # stream.write(data)
                ...

async def main():
    async with r.pubsub() as pubsub:
        await pubsub.subscribe(AUDIO_IN_CHANNEL, AUDIO_OUT_CHANNEL)
        # future = asyncio.create_task(reader(pubsub))

        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            print(len(data))
            stream.write(data)

            await r.publish(AUDIO_IN_CHANNEL, data)

        await future


if __name__ == "__main__":
    asyncio.run(main())
