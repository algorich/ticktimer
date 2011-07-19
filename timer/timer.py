# Copyright (c) 2011 Hugo Henriques Maia Vieira
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import pygst, gst
from time import sleep
import pynotify

class Timer(object):

    def __init__(self, minutes=0, seconds=0):
        try:
            self._minutes = int(minutes)
            self._seconds = int(seconds)
        except ValueError:
            raise ValueError, 'minutes and seconds should be numbers or numerical strings'

    def verbose_run(self):
        time = self._minutes * 60 + self._seconds
        for s in range(time):
            os.system('clear')
            minutes, seconds = divmod(time, 60)
            time -= 1
            print '%02d:%02d' % (minutes, seconds)
            sleep(1)
        self._notify()
        self._play_sound()

    def run(self):
        time = self._minutes * 60 + self._seconds
        for s in range(time):
            sleep(1)
        self._notify()
        self._play_sound()

    def _play_sound(self):
        player = gst.element_factory_make("playbin", "player")
        player.set_state(gst.STATE_NULL)
        sound_uri = 'file://' + os.path.dirname(__file__) + '/timer.mp3'
        player.set_property('uri', sound_uri)
        player.set_state(gst.STATE_PLAYING)
        sleep(4)

    def _notify(self):
        pynotify.init('Timer')
        notification = pynotify.Notification("Time's up!",
                                             '%02d:%02d has passed'
                                                % (self._minutes,self._seconds),
                                             'dialog-ok')
        notification.show()

