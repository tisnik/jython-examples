from javax.swing import JButton
from javax.swing import JFrame


frame = JFrame("Simple GUI",
               defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
               size=(320, 240))


def on_button_clicked(event):
    print 'Button clicked!'


button = JButton('Test', actionPerformed=on_button_clicked)
frame.add(button)
frame.visible = True
