import kivy
kivy.require('1.0.6')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.properties import StringProperty
# FIXME this shouldn't be necessary
from kivy.core.window import Window


class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)


class PicturesApp(App):

    def build(self):
        # the root is created in pictures.kv
        root = self.root
    
        def pixel_alive(self):
            filename = '/Users/niklas/Pixel/PyPsiExpert/results/dac_dac.png'
            try:
                # load the image
                picture = Picture(source=filename)
                # add to the main field
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

        bt1 = Button(text='DacDac', font_size=14,height=24, width=24)
        root.add_widget(bt1)
        bt1.bind(on_release=pixel_alive)



if __name__ == '__main__':
    PicturesApp().run()
