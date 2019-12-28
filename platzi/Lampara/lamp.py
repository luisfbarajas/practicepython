# -*- coding: utf-8 -*-

class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turn_on = is_turned_on

    def turn_on(self):
        self._is_turn_on = True
        self._display_image()

    def turn_off(self):
        self._is_turn_on = False
        self._display_image()
    
    def _display_image(self):
        if self._is_turn_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])