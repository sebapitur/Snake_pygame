# Snake_pygame
sudo apt-get install python3-tk
It is highly recommended to read the report to get a light introduction to  emulation. The report is relevant, eventhough you want to contribute to another emulator, or create your own.

If you've read the report and want more explicit details, have a look at the Pan Docs.

If you are looking to make a bot or AI, you can find all the external components in the PyBoy Documentation. There is also a short example on our Wiki page Scripts, AI and Bots as well as in the examples directory. If more features are needed, or if you find a bug, don't hesitate to make an issue here on GitHub, or write on our Discord channel.


# Installation

The instructions are simple, if you already have a functioning Python environment on your machine.

    Install SDL2 through your package manager:
        Ubuntu: sudo apt install libsdl2-dev
        Fedora: sudo dnf install SDL2-devel
        macOS: brew install sdl2

    Install PyBoy using pip install pyboy (add --user if your system asks)

Now you're ready! Either use PyBoy directly from the terminal $ pyboy file.rom or use it in your Python scripts:

from pyboy import PyBoy
pyboy = PyBoy('ROMs/gamerom.gb')
while not pyboy.tick():
    pass

If you need more details, or if you need to compile from source, check out the detailed installation instructions. We support: macOS, Raspberry Pi (Raspbian), Linux (Ubuntu), and Windows 10.

At the Wiki page, you will also find out how to interface with PyBoy from your own project: Wiki.
Contributors

Thanks to all the people, who have contributed to the project!
Original Developers

    Asger Anders Lund Hansen - AsgerLundHansen
    Mads Ynddal - baekalfen
    Troels Ynddal - troelsy

# GitHub Collaborators

    Kristian Sims - krs013

# Student Projects

    Rewind Time: Jacob Olsen - JacobO1
    Link Cable: Jonas Flach-Jensen - thejomas

# Contribute

Any contribution is appreciated. The currently known errors are registered in the Issues tab. Feel free to take a swing at any one of them.

For the more major features, there are the following that you can give a try. They are also described in more detail in the project list:

    Color
    Link Cable
    (Experimental) AI - use the botsupport or game wrappers to train a neural network
    (Experimental) Game Wrappers - make wrappers for popular games

If you want to implement something which is not on the list, feel free to do so anyway. If you want to merge it into our repo, then just send a pull request and we will have a look at it.
