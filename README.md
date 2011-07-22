# TickTimer

This is a timer written in python.

## Command line usage

    $ ticktimer (minutes|minutes:seconds) [-h|--help] [-v|--verbose]

The _--verbose_ option shows a count down timer on the terminal.

### Control the running

You can use some commands to control how _ticktimer_ is running.

#### Pause

Let's say that you run _ticktimer_ like this:

    $ ticktimer 5:30 -v

To pause the time, press `Ctrl+z` and the process you be paused on background.
To get it running again, use the `fg` command.

Now, let's say that you run _ticktimer_ on background, like this:

    $ ticktimer 5:30 &

To pause the time, use the command `fg`, to get the process running on
foreground. Then, press `Ctrl+z` and the process you be paused on background. To
get it running on background again, use the command `bg`.

#### Stop

Let's say that you run _ticktimer_ like this:

    $ ticktimer 5:30 -v

To stop the time, press `Ctrl+c` and the process you be stoped.

Now, let's say that you run _ticktimer_ on background, like this:

    $ ticktimer 5:30 &

To stop the time, use the command `fg`, to get the process running on
foreground. Then, press `Ctrl+c` and the process you be stoped.


## Install

Just run the _install_ script.

    $ ./install


## The goals

- Work on command line
- Play a sound when times up
- Pause function
- Graphical interface integrated with unity
- Manage presets


## License

Copyright (c) 2011 Hugo Henriques Maia Vieira

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

