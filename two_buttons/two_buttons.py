import sys
from javax.swing import JButton
from javax.swing import JFrame
from java.awt import Component, GridLayout

frame = JFrame("Simple GUI",
               defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
               size=(320, 240))

contentPane = frame.getContentPane()
contentPane.setLayout(GridLayout(2, 1))


def on_button_clicked(event):
    print 'Button clicked!'


button1 = JButton('Test', actionPerformed=on_button_clicked)
button2 = JButton('Quit', actionPerformed=lambda event:sys.exit())

frame.add(button1)
frame.add(button2)
frame.visible = True
