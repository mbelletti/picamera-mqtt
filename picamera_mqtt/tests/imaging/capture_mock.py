#!/usr/bin/env python3
"""Capture an image."""
import json

from picamera_mqtt.imaging import imaging
from picamera_mqtt.util import files


def main():
    camera = imaging.MockCamera()
    print('Capturing image...')
    image_pil = camera.capture_pil(quality=100)
    print('Captured image!')
    print('Saving capture_mock_pil.jpg...')
    image_pil.save('capture_mock_pil.jpg', quality=100)
    print('Saved capture_mock_pil.jpg!')
    print('Converting to base64...')
    image_base64 = imaging.pil_to_base64(image_pil, quality=80)
    print('Converted to base64!')
    message = {'image': image_base64}
    print('Dumping to json...')
    message_json = json.dumps(message)
    print('Dumped to json!')
    print('Loading from json...')
    message = json.loads(message_json)
    print('Loaded from json!')
    image_base64_string = message['image']
    print('Saving capture_mock_final.jpg...')
    files.b64_string_bytes_save(
        image_base64_string, 'capture_mock_final.jpg'
    )
    print('Saved capture_mock_final.jpg!')


# Main program logic follows:
if __name__ == '__main__':
    main()
