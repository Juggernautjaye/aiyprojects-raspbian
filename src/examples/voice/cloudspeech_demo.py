#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech

from aiy.board import Board, Led

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')

    aiy.audio.get_recorder().start()

    with Board() as board:
        while True:
            print('Press the button and speak')
            board.button.wait_for_press()
            print('Listening...')
            text = recognizer.recognize()
            if not text:
                print('Sorry, I did not hear you.')
            else:
                print('You said "', text, '"')
                if 'turn on the light' in text:
                    board.led.state = Led.ON
                elif 'turn off the light' in text:
                    board.led.state = Led.OFF
                elif 'blink' in text:
                    board.led.state = Led.BLINK
                elif 'goodbye' in text:
                    break


if __name__ == '__main__':
    main()
